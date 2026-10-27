import csv
import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url)


if response.status_code == 200:
    html_content = response.text
    box = []
    
    bs = BeautifulSoup(html_content, "html.parser")
    all_products = bs.find_all(class_ = "product_pod")
    for product in all_products:
        dictionary = {
            "title": product.h3.a['title'],
            "price": product.find(class_ = "price_color").text,
            "url": product.find("a")['href']
        }
        box.append(dictionary)

    with open("books.csv", "w", encoding='utf-8') as file:
        fieldnames = ["title","price","url"]
        writer = csv.DictWriter(file, fieldnames)
        writer.writeheader()
        writer.writerows(box)


else:
    print("wrong:", response.status_code)