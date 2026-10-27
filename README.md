# Books to Scrape - Python Web Scraper

A lightweight and efficient Python web scraper that extracts book data from the "Books to Scrape" sandbox website and saves it into a structured CSV file.

## 🚀 Features
- Fetches HTML content using the `requests` library.
- Parses and navigates the HTML structure using `BeautifulSoup`.
- Extracts key product details:
  - **Title**
  - **Price**
  - **Product URL**
- Exports the collected data automatically into a clean `books.csv` file.

## 🛠 Tech Stack
- **Python 3**
- **Requests** (for HTTP requests)
- **BeautifulSoup4** (for HTML parsing)
- **CSV** (built-in module for data persistence)

## ⚙️ Installation & Usage

1. Clone or download the project folder.
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
