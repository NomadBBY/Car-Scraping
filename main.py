from bs4 import BeautifulSoup
import requests

def fetch_soup(website_url):
    response = requests.get(website_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        return soup
    else:
        print(f"Unable to fetch page: {website_url}")
        return None

def fetch_div(soup, class_name):
    if soup:
        div = soup.find('div', class_=class_name)
        return div
    return None

if __name__ == "__main__":
    link = "https://lv.brcauto.eu/lietoti-auto?city=5&search=1&makes=31473"
    
    soup = fetch_soup(link)
    if soup:

        print("Connection Made")
        print(f"Title of the page: {soup.title.string}")
        div = fetch_div(soup, "cars-container row-3")
        if div:
            print("Found the div with class 'cars-container row-3'")
            print(div)
        else:
            print("Div with class 'cars-container row-3' not found")
            
    else:
        print("Failed to fetch the page")