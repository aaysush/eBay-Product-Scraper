# eBay-Product-Scraper

# eBay Dynamic Content Scraper

A Python-based web scraping tool that extracts product information from eBay listings using Selenium WebDriver. The scraper handles dynamic content loading and implements human-like behavior patterns to minimize detection risk.

## Features

- **Dynamic Content Handling**: Uses Selenium to render JavaScript-heavy pages
- **Anti-Detection Measures**: Implements random delays, scrolling simulation, and custom user agents
- **Robust Error Handling**: Gracefully handles missing elements and network issues
- **Headless Operation**: Runs in background mode for automated workflows
- **Flexible Configuration**: Easy to modify Chrome options and scraping parameters

## Prerequisites

- Python 3.x
- ChromeDriver (compatible with your Chrome browser version)
- Required Python packages:
  ```bash
  pip install selenium
  ```

## Installation

1. Download ChromeDriver from the official site
2. Update the ChromeDriver path in the script:
   ```python
   service = Service(r"path/to/your/chromedriver.exe")
   ```
3. Ensure Chrome browser is installed on your system

## Usage

### Basic Usage

```python
from your_script import fetch_dynamic_content

url = "https://www.ebay.com/itm/your-product-id"
success = fetch_dynamic_content(url)

if success:
    print("Scraping completed successfully")
```

### Interactive Mode

Run the script directly to enter URLs interactively:

```bash
python ebay_scraper.py
```

You'll be prompted to enter an eBay product URL, and the scraper will extract:
- Product title
- Current price
- Discount information (if available)

## Code Structure

### Core Functions

#### `random_delay(min_seconds=2, max_seconds=5)`
Introduces random delays between actions to simulate human browsing behavior.

**Parameters:**
- `min_seconds` (int): Minimum delay duration
- `max_seconds` (int): Maximum delay duration

#### `fetch_dynamic_content(url)`
Main scraping function that extracts product information from eBay listings.

**Parameters:**
- `url` (str): eBay product URL to scrape

**Returns:**
- `bool`: True if scraping successful, False otherwise

**Extracts:**
- Product title from `.x-item-title__mainTitle`
- Price from `.x-price-primary`
- Discount from `.x-price-transparency--discount`

## Configuration Options

### Chrome Options
The scraper uses the following Chrome configurations:

```python
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without GUI
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--ignore-certificate-errors")  # Ignore SSL errors
chrome_options.add_argument("user-agent=Mozilla/5.0...")  # Custom user agent
```

### Timeout Settings
- Page load timeout: 15 seconds
- Element wait timeout: 15 seconds

## Example Output

```
Enter an eBay URL to scrape: https://www.ebay.com/itm/155465650023
Product Title: Men's Black Streetwear Techwear Heavy Cargo Trouser Pants
Price: US $288.00
Discount: Was US $320.00 (10% off)
Scraping successful!
```

## Error Handling

The scraper includes comprehensive error handling for:
- Missing product elements
- Page load failures
- Network connectivity issues
- WebDriver initialization problems

When elements are not found, default "not found" messages are returned instead of crashing.

## Limitations

- Requires ChromeDriver installation and maintenance
- May need updates when eBay changes their HTML structure
- Rate limiting may affect high-volume scraping
- Headless mode may be detected by advanced anti-bot systems

## Best Practices

1. **Respect Rate Limits**: Add appropriate delays between requests
2. **Update ChromeDriver**: Keep ChromeDriver version compatible with your Chrome browser
3. **Monitor for Changes**: eBay may update their CSS classes; update selectors accordingly
4. **Legal Compliance**: Ensure your usage complies with eBay's Terms of Service
5. **Error Monitoring**: Implement logging for production use

## Troubleshooting

### Common Issues

**ChromeDriver not found:**
- Verify the ChromeDriver path in the Service configuration
- Ensure ChromeDriver is executable

**Element not found:**
- Check if eBay has updated their HTML structure
- Verify the URL is accessible and contains the expected content

**Timeout errors:**
- Increase wait timeouts for slower connections
- Check if the page is loading correctly

## Extensions

The codebase can be extended to:
- Support multiple product URLs
- Add database storage for scraped data
- Implement proxy rotation (see proxy variant)
- Add product comparison features
- Schedule automated scraping tasks

## License

This tool is provided for educational purposes. Users are responsible for ensuring compliance with applicable terms of service and legal requirements.
 This project demonstrates how to scrape product details from eBay webpages using Selenium, BeautifulSoup, and ChromeDriver. The scraper mimics human-like behavior to fetch dynamic content such as product title, price, and discount information by interacting with the webpage.
The primary goal of this project is to provide an efficient and reusable template for web scraping that adheres to best practices, including handling dynamic content and reducing the likelihood of detection.

Features:-
-Dynamic Content Handling: Uses Selenium to fetch content that requires JavaScript rendering.
-Human-like Behavior: Introduces random delays and scrolling actions to mimic real user interactions, minimizing the chances of being detected as a bot.
-Customizable Options: Runs in headless mode for faster performance or visible mode for debugging.
-Error Handling: Gracefully manages missing elements, ensuring robust execution.
-Extensibility: Code is modular and can be extended to scrape additional elements.

How It Works
-Setup: The script initializes a Selenium WebDriver with configurable Chrome options.
-Interaction: Opens the provided eBay URL, simulates scrolling, and waits for the required elements to load.
-Scraping: Extracts product title, price, and discount details.


Prerequisites

Python 3.x
Selenium
ChromeDriver (compatible with your Chrome browser version)
Additional Python Libraries: random, time


NOTE:
There is a additional file named eBAY_custom_proxy.py which can be used to integrate your own proxy services(eg.BrightData)
or u can use it locally using cron job


 
 ### Example Execution()

Below is an example of the script in action:

**Input:**  
User-provided eBay URL:  
`https://www.ebay.com/itm/155465650023?_skw=discounted+pant...`

**Execution Output:**  
Enter an eBay URL to scrape: https://www.ebay.com/itm/155465650023?_skw=discounted+pant...
Product Title: Men's Black Streetwear Techwear Heavy Cargo Trouser Pants H-G B.L.P-04.V2/BLCK  
Price: US $288.00  
Discount: Was US $320.00 (10% off)  
Scraping successful!


### Example Execution

Below is an example of the script in action:

**Execution Terminal Output:**  
 
PS C:\Users\Administrator\Desktop\Price Tracker> & C:/Users/Administrator/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/Administrator/Desktop/Price Tracker/final_ebay_scrapper.py"

Enter an eBay URL to scrape: https://www.ebay.com/itm/155465650023?_skw=discounted+pant&itmmeta=01JYA2N6PD30K5BSRGGDVPTHME&hash=item2432798f67:g:gccAAOSwRjxmqkJf&itmprp=enc%3AAQAKAAAA8FkggFvd1GGDu0w3yXCmi1eUXqsNdyFu%2FdKF5Sf%2FrkSA%2Fk9jd3zopD4E3Dc%2BtzXgFYsTcwyPRNbWym%2FAkBS0hfe%2FU6ecdWh9rVeEUOROgEnn6xMJvwCFqDrrHxNU75jplk6Ut5endsF%2FK8mVp0ItIUNl1ndGD8mv6hconV7rCyF0SOKcnyq%2BNUgZFnzEOxGX3tlQyWP0LCEVoQ1%2BMS9Ku6F12SYKetgr8kyO3E6qarSyVpswMvddnRAF%2BM%2Bx36qkaSAL6Jw%2FUs5ws6H%2Fq8kJoGx34vTwQGNJMCNFCVWRnfU8ExN2XpIH8ASnCLkEw8NhrQ%3D%3D%7Ctkp%3ABk9SR6zr1MLyZQ

DevTools listening on ws://127.0.0.1:51105/devtools/browser/b363caf0-3820-44a0-a0b3-b4b014e3a84f

Product Title: Men's Black Streetwear Techwear Heavy Cargo Trouser Pants H-G B.L.P-04.V2/BLCK
Price: US $288.00
Discount: Was US $320.00 (10% off)
Scraping successful!
