import requests
import bs4

res = requests.get("https://www.ss.com/lv/transport/cars/bmw/3-series/")
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")

print(soup.find("tr", {"id": "tr_55103202"}))