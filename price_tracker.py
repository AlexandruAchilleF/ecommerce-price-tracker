from playwright.sync_api import sync_playwright
import pandas as pd
import time

def scrape_laptops():
    product_data = []

    with sync_playwright() as p:
        # headless=False helps you see the browser actions during debugging
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print("Accessing the website...")

        page.goto("https://altex.ro/laptopuri/cpl/", timeout=60000)

        # Wait for the page to fully load
        page.wait_for_load_state('domcontentloaded')
        page.wait_for_selector('div.Product', timeout=60000)

        # Scroll down to trigger lazy loading of images and elements
        page.mouse.wheel(0, 1000)
        time.sleep(2)

        print("Searching for products...")

        # Locate all product containers using the class found in DevTools
        products = page.locator('div.Product').all()

        print(f"Found {len(products)} products. Extracting data...")

        for product in products:
            try:
                title_locator = product.locator('.Product-name').first
                title = title_locator.inner_text(timeout=2000) if title_locator.count() > 0 else "No title"

                price_locator = product.locator('[class*="Price"]').first
                raw_price = price_locator.inner_text(timeout=2000) if price_locator.count() > 0 else "0"

                product_data.append({
                    'Title': title.strip(),
                    'Raw_Price': raw_price.strip()
                })
            except Exception as e:
                continue

        browser.close()

    # Data Cleaning with Pandas
    print("\nCleaning the extracted data...")
    df = pd.DataFrame(product_data)

    if not df.empty:
        # Remove letters and whitespaces
        df['Clean_Price'] = df['Raw_Price'].str.replace(r'[a-zA-Z\s]', '', regex=True)

        # Remove thousand separators (dots) and replace comma with dot for decimals
        df['Clean_Price'] = df['Clean_Price'].str.replace('.', '', regex=False)
        df['Clean_Price'] = df['Clean_Price'].str.replace(',', '.', regex=False)

        # Extract just the numeric part to avoid hidden characters
        df['Clean_Price'] = df['Clean_Price'].str.extract(r'(\d+\.\d+|\d+)')

        # Convert to float for numerical operations
        df['Clean_Price'] = df['Clean_Price'].astype(float)

        # Sort by price (ascending)
        df = df.sort_values(by='Clean_Price')

        # Export to a CSV file
        df.to_csv('altex_laptops_cleaned.csv', index=False, encoding='utf-8')
        print("\nFILE SAVED: altex_laptops_cleaned.csv")

        # Display the top 5 cheapest laptops
        print("\nTop 5 Cheapest Laptops:")
        print(df[['Title', 'Clean_Price']].head(5))
    else:
        print("No data extracted")


if __name__ == "__main__":
    scrape_laptops()