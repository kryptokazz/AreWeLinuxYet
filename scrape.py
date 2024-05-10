import requests
from bs4 import BeautifulSoup
import json

# URL of the website to scrape
url = "https://www.opensourcealternative.to/?sort-desc=github-stars"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all items with class "w-dyn-item"
items = soup.find_all(class_="w-dyn-item")

# Initialize an empty list to store the scraped data
scraped_data = []

# Loop through each item
for item in items:
    # Extract product name
    product_name = item.find("h3", class_="freelancer-card-name").text.strip()
    
    # Extract description
    description = item.find("p", class_="paragraph-2-front").text.strip()
    
    # Extract link
    link = "https://www.opensourcealternative.to" + item.find("a")["href"]

    # Append the extracted data to the list
    scraped_data.append({
        "productName": product_name,
        "description": description,
        "link": link
    })

# Print the scraped data
print(json.dumps(scraped_data, indent=2))

