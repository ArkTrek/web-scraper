import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import threading
import itertools
import sys
import time

# Loading animation function
def loading_animation(message="Loading"):
    spinner = itertools.cycle(['|', '/', '-', '\\'])
    sys.stdout.write(f"{message}... ")
    sys.stdout.flush()
    while not stop_animation_flag:
        sys.stdout.write(next(spinner))  # Write the next spinner character
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')  # Erase the spinner character

# Scraping function
def scrape_to_csv(url, output_csv):
    global stop_animation_flag

    # Start the loading animation in a separate thread
    stop_animation_flag = False
    animation_thread = threading.Thread(target=loading_animation)
    animation_thread.start()
    
    try:
        # Add headers to mimic a browser request
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
        
        # Fetch the webpage content
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Parse the webpage content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract the table
        table = soup.find('table')
        if not table:
            print("\nNo table found on the page!")
            stop_animation_flag = True
            animation_thread.join()
            return
        
        # Extract headers
        try:
            headers = [header.text.strip() for header in table.find_all('th')]
            if not headers:
                print("\nNo headers found. Using default column names.")
                sample_row = table.find_all('tr')[1].find_all('td')
                headers = [f"Column{i+1}" for i in range(len(sample_row))]
        except IndexError:
            print("\nTable structure is invalid or empty!")
            stop_animation_flag = True
            animation_thread.join()
            return
        
        # Extract rows
        data = []
        rows = table.find_all('tr')
        for row in rows:
            cells = [cell.text.strip() for cell in row.find_all('td')]
            if cells:
                data.append(cells)
        
        # Validate data before creating the DataFrame
        if not data:
            print("\nNo data rows found to save!")
            stop_animation_flag = True
            animation_thread.join()
            return
        
        # Create and save the DataFrame
        df = pd.DataFrame(data, columns=headers)
        df.to_csv(output_csv, index=False)
        print(f"\nData saved to {output_csv}")
    
    except requests.exceptions.RequestException as e:
        print(f"\nFailed to fetch the webpage: {e}")
    
    except ValueError as e:
        print(f"\nError creating DataFrame: {e}")
        print("Data rows:")
        print(data)
        print("Headers:")
        print(headers)
    
    finally:
        stop_animation_flag = True
        animation_thread.join()

if __name__ == "__main__":
    # Get URL input from the user
    url = input("Enter the URL of the webpage to scrape: ").strip()
    
    # Dynamic output file naming
    output_csv = f"scraped_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    # Start the scraping process
    scrape_to_csv(url, output_csv)
