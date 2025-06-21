from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import random
import requests
import re
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
#-----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#use this on a set pof realiable ips
successful_proxies = []
 

def get_proxy_list():
    # Fetch proxies from spys.me
    spys_url = "https://spys.me/proxy.txt"
    response = requests.get(spys_url)
    if response.status_code == 200:
        regex = r"[0-9]+(?:\.[0-9]+){3}:[0-9]+"
        proxies = re.findall(regex, response.text)
        print(f"Added {len(proxies)} proxies from spys.me.")
        return proxies
    else:
        print(f"Failed to fetch proxies from spys.me. Status code: {response.status_code}")
        return []








#--------------------------------------------------------------------------------------------
def test_proxy(proxy, url):
    try:
        # Configure Chrome Options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument(f"--proxy-server={proxy}")

        # Start WebDriver
        service = Service(r"C:\Users\Administrator\Desktop\Price Tracker\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.set_page_load_timeout(15)

        # Test proxy by navigating to the URL
        driver.get(url)
        print(f"Proxy {proxy} succeeded. Page Title: {driver.title}")
        driver.quit()
        return True
    except Exception as e:
        print(f"Proxy {proxy} failed. Error: {e}")
        return False


def fetch_dynamic_content(url, proxy=None):
    try:
        # Configure Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--ignore-certificate-errors")

        # Add proxy if provided
        if proxy:
            chrome_options.add_argument(f"--proxy-server={proxy}")

        # Path to ChromeDriver
        service = Service(r"C:\Users\Administrator\Desktop\Price Tracker\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Open the URL
        driver.get(url)

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
    except Exception as e:
        print(f"Error fetching dynamic content: {e}")

'''
def scrape_with_beautifulsoup(html_code):
        
    from bs4 import BeautifulSoup

    # Load the HTML content
    with open("ebay_source.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")

    # Extract the product title
    h1_element = soup.find("h1", class_="x-item-title__mainTitle")
    product_title_element = h1_element.find("span", class_="ux-textspans ux-textspans--BOLD") if h1_element else None
    product_title = product_title_element.text.strip() if product_title_element else "Product title not found"

    # Extract the price
    price_primary = soup.find("div", class_="x-price-primary", attrs={"data-testid": "x-price-primary"})
    price_element = price_primary.find("span", class_="ux-textspans") if price_primary else None
    price = price_element.text.strip() if price_element else "Price not found"

    # Extract the discount information
    discount_container = soup.find("span", class_="x-price-transparency--discount", attrs={"data-testid": "ux-textual-display"})
    discount_element = discount_container.find("span", class_="ux-textspans ux-textspans--EMPHASIS") if discount_container else None
    discount = discount_element.text.strip() if discount_element else "Discount information not found"

    # Output the results
    print("Product Title:", product_title)
    print("Price:", price)
    print("Discount:", discount)
'''

        
if __name__ == "__main__":
    # Get and test proxies
    proxy_list = get_proxy_list()
    test_url = "https://www.ebay.com"  # eBay URL for proxy testing

    for proxy in proxy_list:
        if test_proxy(proxy, test_url):
            successful_proxies.append(proxy)
        if len(successful_proxies) >= 1:  # Use more proxies if needed
            break

    print(f"Successful Proxies: {successful_proxies}")

    # Scrape URLs with successful proxies
    url_to_scrape = input("Enter an eBay URL to scrape: ") 
    proxy = random.choice(successful_proxies) if successful_proxies else None

    if proxy:
        fetch_dynamic_content(url_to_scrape, proxy=None)
