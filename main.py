import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Function to scrape tables and save them to CSV
def scrape_to_csv(url, output_csv):
    try:
        # Add headers to mimic a browser request
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
        
        # Fetch the webpage content
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Parse the webpage content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract all tables from the page
        tables = soup.find_all('table')
        if not tables:
            print("No tables found on the page!")
            return
        
        # Process each table
        for index, table in enumerate(tables, start=1):
            # Extract headers
            headers = [header.text.strip() for header in table.find_all('th')]
            
            # Extract rows (cells)
            data = []
            rows = table.find_all('tr')
            for row in rows:
                cells = [cell.text.strip() for cell in row.find_all(['td', 'th'])]  # Capture both <td> and <th>
                if cells:
                    data.append(cells)
            
            # Truncate headers and rows to the first 6 columns
            max_columns = 6
            truncated_headers = headers[:max_columns] if headers else [f"Column{i+1}" for i in range(max_columns)]
            truncated_data = [row[:max_columns] for row in data]
            
            # Create the DataFrame
            df = pd.DataFrame(truncated_data, columns=truncated_headers)
            
            # Save the DataFrame to CSV
            output_file = output_csv if len(tables) == 1 else f"{output_csv.split('.csv')[0]}_table{index}.csv"
            df.to_csv(output_file, index=False)
            print(f"Table {index} saved to {output_file}")
    
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch the webpage: {e}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Get URL input from the user
    url = input("Enter the URL of the webpage to scrape: ").strip()
    
    # Dynamic output file naming
    output_csv = f"scraped_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    # Start the scraping process
    scrape_to_csv(url, output_csv)
