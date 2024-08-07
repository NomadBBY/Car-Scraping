from bs4 import BeautifulSoup
import requests

def fetch_soup(website_url: str):
    response = requests.get(website_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        return soup
    else:
        print(f"Unable to fetch page: {website_url}")
        return None
    
def fetch_div(soup, div_name: str, class_name: str):
    if soup:
        div = soup.find(div_name, class_=class_name)
        return div
    return None

def fetch_subtitles(div, subtitle_name: str, subtitle_class_name:str):
    if div:
        #subtitles = div.find_all('p', class_='cars__subtitle')
        subtitles = div.find_all(subtitle_name, class_=subtitle_class_name)
        return subtitles
    return []

def parse_price(price_str):
    return float(price_str.replace('€', '').replace(',', ''))

def sort_cars_by_price(cars):
    return sorted(cars, key=lambda x: parse_price(x[2].getText().strip()))

def fetch_and_print_subtitles(div, title_tag, title_class, spec_tag, spec_class, price_tag, price_class):
    titles = fetch_subtitles(div, title_tag, title_class)
    specs = fetch_subtitles(div, spec_tag, spec_class)
    prices = fetch_subtitles(div, price_tag, price_class)
    
    if titles and specs and prices:
        cars = list(zip(titles, specs, prices))
        sorted_cars = sort_cars_by_price(cars)
        
        for i, (title, spec, price) in enumerate(sorted_cars, 1):
            print(f"Car {i}:")
            print(f"{title.getText().strip()} - {spec.getText().strip()}")
            print(f"Price: {price.getText().strip()}")
            print("-" * 100)
    elif not titles:
        print(f"No titles with class '{title_class}' found inside the div")
    elif not specs:
        print(f"No specs with class '{spec_class}' found inside the div")
    elif not prices:
        print(f"No prices with class '{price_class}' found inside the div")
    else:
        print("No matching titles, specs, and prices found")

link = "https://lv.brcauto.eu/lietoti-auto?city=5&search=1&makes=31473"

soup = fetch_soup(link)
if soup:
    print("Connection Made", '\n')
    print(f"Title of the page: {soup.title.string}", '\n')

    div = fetch_div(soup, 'div' , "cars-container row-3")
    if div:
        print("Found the div with class 'cars-container row-3'")
        print(div.prettify())
    else:
        print("Div with class 'cars-container row-3' not found")
        
else:
    print("Failed to fetch the page")

fetch_and_print_subtitles(div, 'h2', "cars__title", 'p', "cars__subtitle", 'div', 'w-full lg:w-auto cars-price text-right pt-1')
