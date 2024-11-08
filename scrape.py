import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize the WebDriver
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

# Open the Amazon page
url = "https://www.amazon.in/s?k=phone&rh=n%3A6612025031&ref=nb_sb_noss"
driver.get(url)

# Scroll to the bottom of the page to load all products
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Close the WebDriver
driver.quit()

# Find all product containers
products = soup.find_all('div', {'data-component-type': 's-search-result'})

# Lists to store product details
product_names = []
prices = []
ratings = []
sellers = []

# Extract details for each product
for product in products:
    # Product Name
    name = product.h2.text.strip() if product.h2 else 'N/A'
    product_names.append(name)

    # Price
    price = product.find('span', 'a-price-whole')
    price = price.text.strip() if price else 'N/A'
    prices.append(price)

    # Rating
    rating = product.find('span', 'a-icon-alt')
    rating = rating.text.strip() if rating else 'N/A'
    ratings.append(rating)

    # Seller Name (if available)
    seller = product.find('span', 'a-size-small a-color-base')
    seller = seller.text.strip() if seller else 'N/A'
    sellers.append(seller)

# Debugging: Print the extracted details
print("Product Names:", product_names)
print("Prices:", prices)
print("Ratings:", ratings)
print("Sellers:", sellers)

# Create a DataFrame and save to CSV
df = pd.DataFrame({
    'Product Name': product_names,
    'Price': prices,
    'Rating': ratings,
    'Seller Name': sellers
})

df.to_csv('amazon_products.csv', index=False)

print("Data has been scraped and saved to amazon_products.csv")
