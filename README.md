# eBay-Product-Scraper
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
There is a additional file named scrapper_custom_proxy.py which can be used to integrate your own proxy services(eg.BrightData)
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
