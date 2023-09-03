import re
import json
import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('meghana.html', 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the script tag containing JSON-LD data
menu_script = soup.find("script", type="application/ld+json")

if menu_script:
    # Extract the content of the script tag
    script_content = menu_script.contents[0]
    
    # Parse the JSON data
    try:
        menu_data = json.loads(script_content)
        
        # Extract menu items
        menu_sections = menu_data.get("hasMenuSection", [])
        
        # Prepare a list to store extracted data
        menu_list = []
        
        for section in menu_sections:
            section_name = section.get("name", "")
            for item in section.get("hasMenuItem", []):
                item_name = item.get("name", "")
                item_price = item.get("offers", {}).get("price", "")
                menu_list.append({"Section": section_name, "Item": item_name, "Price": item_price})
        
        # Save data to CSV file
        csv_file = "zomato_menu.csv"
        with open(csv_file, "w", newline="", encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["Section", "Item", "Price"])
            writer.writeheader()
            writer.writerows(menu_list)
        
        print(f"Menu data saved to {csv_file}")
    except json.JSONDecodeError:
        print("Error decoding JSON data.")
else:
    print("Menu data not found in the HTML content.")
