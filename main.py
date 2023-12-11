import json
import requests
from bs4 import BeautifulSoup

from core.config import URL, DOMAIN, HEADERS


def get_html(url, header=HEADERS):
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        return response.text
    else:
        raise ValueError(f"Error in request to\
                          {url} code {response.status_code}")

def processing(html):
    soup = BeautifulSoup(html, 'lxml').find("div", {"class": "grid__catalog"}
        ).find_all("a", {"class": "x-product-card__link x-product-card__hit-area"})
    
    source = []

    for a in soup:
        product_url = DOMAIN + a.get('href')
        product_brand = a.find("div", {"class": "x-product-card-description__brand-name"}).text
        product_name = a.find("div", {"class":"x-product-card-description__product-name"}).text
        product_price = a.find("span", 
            {"class": "x-product-card-description__price-WEB8507_price_no_bold"}).text
        product_img = a.find("img", {"class": "x-product-card__pic-img"})

        img = product_img.get("src") if product_img is not None else "/no_image"

        source.append({
        "url": product_url,
        "brand": product_brand,
        "name": str(product_name).strip(),
        "price": product_price,
        "img": DOMAIN + img
        })

    return source

def run():
    info = []
    for page in range(1, 4):
        html = get_html(URL+str(page))
        source = processing(html)
        info.extend(source)
        print(f"Page {page} is done")

    with open ("info.json", "w") as file:
        json.dump(info, file, indent=4, ensure_ascii=False)


run()