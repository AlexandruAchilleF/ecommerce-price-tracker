# Altex Laptop Price Scraper

A Python web scraping project that extracts laptop data (titles and prices) from [Altex.ro](https://altex.ro/), cleans the data, and exports it into a structured CSV format.

This project demonstrates how to handle dynamically loaded content (JavaScript/lazy loading) using Playwright and how to clean raw text data into numerical formats using Pandas.

## Features
* **Dynamic Web Scraping:** Uses Playwright to launch a Chromium browser, navigate the page, and simulate scrolling to trigger lazy-loaded product elements.
* **Robust Data Extraction:** Locates product containers and safely extracts titles and raw price strings.
* **Data Cleaning & Transformation:** Uses Pandas and Regular Expressions (Regex) to strip currencies and letters, remove thousands separators, and convert comma decimals to standard floats.
* **Data Export:** Sorts the laptops by price (ascending) and exports the cleaned dataset to `altex_laptops_cleaned.csv`.

## Tech Stack
* **Python 3.x**
* **[Playwright](https://playwright.dev/python/):** For browser automation and scraping dynamic content.
* **[Pandas](https://pandas.pydata.org/):** For data manipulation, cleaning, and CSV export.

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd <your-repository-folder>
   ```

2. **Install dependencies:**
   Make sure you have Python installed. Then, install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright browsers:**
   Since Playwright automates real browsers, you need to install the Chromium binaries:
   ```bash
   playwright install chromium
   ```

## Usage

Run the scraper from your terminal:
```bash
python price_tracker.py
```

**What the script does when running:**
1. A Chromium browser will launch in visible mode (`headless=False`) so you can watch the automation in real-time.
2. It will navigate to the Altex laptops section and scroll down to load more products.
3. The terminal will log the scraping progress and output the top 5 cheapest laptops found.
4. A file named `altex_laptops_cleaned.csv` will be generated in your project directory containing the full sorted list. *(Note: This file is added to `.gitignore` and is not tracked in this repository).*

## Disclaimer
This project is meant for educational purposes to practice web scraping, DOM manipulation, and data cleaning. Please respect the target website's `robots.txt` and terms of service when running scrapers.