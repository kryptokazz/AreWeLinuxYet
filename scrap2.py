import requests
from bs4 import BeautifulSoup
import json

# URL of the website to scrape
url = "https://www.opensourcealternative.to/?sort-desc=github-stars"

# Function to scrape data from a single page
def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.find_all(class_="w-dyn-item")
    scraped_data = []
    for item in items:
        product_name = item.find("h3", class_="freelancer-card-name").text.strip()
        description = item.find("p", class_="paragraph-2-front").text.strip()
        link = "https://www.opensourcealternative.to" + item.find("a")["href"]
        scraped_data.append({
            "productName": product_name,
            "description": description,
            "link": link
        })
    return scraped_data

# Function to scrape all pages
def scrape_all_pages(base_url):
    all_data = []
    page_num = 1
    while True:
        page_url = f"{base_url}&page={page_num}"
        page_data = scrape_page(page_url)
        if not page_data:  # If no more data is found, break the loop
            break
        all_data.extend(page_data)
        page_num += 1
    return all_data

# Scrape all pages
scraped_data = scrape_all_pages(url)

# Print the scraped data
print(json.dumps(scraped_data, indent=2))

