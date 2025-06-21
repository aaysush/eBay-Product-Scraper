from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def random_delay(min_seconds=2, max_seconds=5):
    """Introduces a random delay to mimic human behavior."""
    delay = random.uniform(min_seconds, max_seconds)
    time.sleep(delay)

def fetch_dynamic_content(url):
    try:
        # Configure Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Use headless mode for faster operation (remove for visible browser)
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
        
        # Path to ChromeDriver
        service = Service(r"C:\Users\Administrator\Desktop\Price Tracker\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Open the URL
        driver.get(url)
        random_delay()

        # Simulate scrolling behavior
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        random_delay()

        # Wait for specific elements to load
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "x-item-title__mainTitle"))
        )

        # Extract the title, price, and discount
        try:
            title = driver.find_element(By.CLASS_NAME, "x-item-title__mainTitle").text
        except:
            title = "Title not found"

        try:
            price = driver.find_element(By.CLASS_NAME, "x-price-primary").text
        except:
            price = "Price not found"

        try:
            discount = driver.find_element(By.CLASS_NAME, "x-price-transparency--discount").text
        except:
            discount = "Discount not found"

        print("Product Title:", title)
        print("Price:", price)
        print("Discount:", discount)

        driver.quit()
        return True  # Successful scrape
    except Exception as e:
        print(f"Scraping failed. Error: {e}")
        return False  # Failed scrape


if __name__ == "__main__":
    url_to_scrape = input("Enter an eBay URL to scrape: ")
    if fetch_dynamic_content(url_to_scrape):
        print("Scraping successful!")
    else:
        print("Failed to scrape the content.")

list_of_products = []

'''
def add_products(link):
    link = input('give product link')
    list_of_products.append(link)

def sub_products(link):
    # Code to remove product from the list
'''
