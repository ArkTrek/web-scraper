# 🕸️ Web Scraper

This Python-based project uses **BeautifulSoup** 🥣 and **Pandas** 🐼 to scrape HTML tables from a given webpage 🌐 and save the data into a CSV file 📂. It includes a user-friendly terminal-based loading animation ⏳ to enhance the experience during the scraping process.

---

## ✨ Features
- 🌍 **Web Scraping**: Extracts HTML tables from the provided URL.
- 📝 **CSV Export**: Saves the extracted data into a dynamically named CSV file.
- 🛡️ **Error Handling**: Gracefully handles missing data, invalid URLs, and empty tables.
- 🎡 **Loading Animation**: Displays a fun spinner during the scraping process.
- 🔖 **Dynamic Column Names**: Automatically generates column headers if not present in the table.

---

## 📦 Requirements
### 🛠️ Dependencies
Ensure you have Python 3.6+ installed, and install the required libraries:

```bash
pip install -r requirements.txt
```

Your `requirements.txt` should include:

```plaintext
beautifulsoup4==4.12.2
pandas==1.5.3
requests==2.31.0
```

---

## 🚀 How to Use
1. **Clone the repository**:

   ```bash
   git clone https://github.com/arktrek/web-scraper.git
   cd web-scraper
   ```

2. **Run the script**:

   ```bash
   python main.py
   ```

3. **Input the URL**:  
   Enter the URL of a webpage containing an HTML table (e.g., [W3Schools Tables](https://www.w3schools.com/html/html_tables.asp)) when prompted:

   ```plaintext
   Enter the URL of the webpage to scrape: https://www.w3schools.com/html/html_tables.asp
   ```

4. **Results**:  
   - Data is saved into a CSV file with a timestamped name like `scraped_data_YYYYMMDD_HHMMSS.csv`.  
   - Look for the file in the current directory 📂.

---

## 🧾 Example Output
Here’s an example of how the scraped data may look:

| 🧑 Name       | 🌎 Country   | 🔢 Age  |
|---------------|-------------|---------|
| ABCD          | INDIA       | 25      |
| abcd          | USA         | 30      |

The above table is saved as `scraped_data_20241205_120000.csv`.

---

## 📂 File Structure
```
web-scraper-with-csv/
│
├── main.py             # 🚀 Main script for scraping and exporting
├── requirements.txt    # 📦 List of dependencies
└── README.md           # 📖 Documentation
```

---

## 🤝 Contributions
Contributions are welcome! 🎉 To contribute:
1. 🍴 Fork this repository.
2. 🛠️ Create a feature branch (`git checkout -b feature-branch-name`).
3. ✍️ Commit your changes (`git commit -m "Add feature"`).
4. 🔄 Push to the branch (`git push origin feature-branch-name`).
5. 📩 Open a pull request.

---

## 🧑‍💻 Author
Developed by **Arpit**.  

💌 Contact me at [bitstoday@gmail.com](mailto:bitstoday@gmail.com) or check out my [GitHub Profile](https://github.com/arktrek).

---

Let me know if you'd like to add any more flair or customizations! 🎉
