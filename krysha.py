import json
import requests
from bs4 import BeautifulSoup

URL = "https://krisha.kz/prodazha/kvartiry/"
DOMAIN = "https://krisha.kz/"

HEADERS = {
    "User-Agent":
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.1.1148 (beta) Yowser/2.5 Safari/537.36"
}

def get_html(url, header=HEADERS):
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        return response.text
    else:
        raise ValueError(f"Error code {response.status_code}")
    
def processing(html):
    soup = BeautifulSoup(html, "lxml")
    soup = soup.find_all("div", {"class": "a-card"})
    
    source = []
    for item in soup:
        title = item.find('div', {'class': 'a-card__header-left'}).find('a').text
        price = item.find('div', {'class': 'a-card__price'}).text.strip().replace("\xa0", " ")
        location = item.find('div', {'class': 'a-card__wrapper-subtitle'}).text.strip().replace("\xa0", " ")
        descr = item.find('div', {'class': 'a-card__text-preview'}).text.strip().replace("\xa0", " ")
        img = item.find('a', {'class': 'a-card__image'}).find('img').get('src')

        source.append({
        "title": title,
        "price": str(price).strip(),
        "location": location,
        "description": descr,
        "img": img
        })
        
    return source

def run():
    info = []
    for page in range(1, 4):
        URL = f"https://krisha.kz/prodazha/kvartiry/almaty/?page={page}"
        html = get_html(URL)
        source = processing(html)
        info.extend(source)
        print(f"Page {page} is done")

    with open("krisha.json", "w", encoding="UTF-8") as krisha:
        json.dump(info, krisha, indent=4, ensure_ascii=False)

run()