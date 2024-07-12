import requests
from bs4 import BeautifulSoup

class CarScraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_soup(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return BeautifulSoup(response.content, "html.parser")
        print(f"Unable to fetch page: {url}")
        return None

    def fetch_car_info(self, soup):
        cars_container = soup.find('div', class_="cars-container row-3")
        if not cars_container:
            return []
        
        car_info_list = []
        car_elements = cars_container.find_all('div', class_="cars-container__car")
        
        for car in car_elements:
            title_element = car.find('h2', class_="cars__title")
            subtitle_element = car.find('p', class_="cars__subtitle")
            
            if title_element and subtitle_element:
                link_element = title_element.find('a')
                if link_element:
                    title = link_element.text.strip()
                    link = link_element['href']
                    subtitle = subtitle_element.text.strip()
                    car_info_list.append({
                        'title': title,
                        'link': link,
                        'subtitle': subtitle
                    })
        
        return car_info_list

    def scrape_cars(self, params=None):
        url = self.base_url
        if params:
            url += '?' + '&'.join([f"{k}={v}" for k, v in params.items()])
        
        soup = self.fetch_soup(url)
        if not soup:
            return None

        return self.fetch_car_info(soup)

def print_car_info(car_info_list):
    if car_info_list:
        print(f"Found {len(car_info_list)} car(s):")
        for i, car in enumerate(car_info_list, 1):
            print(f"Car {i}:")
            print(f"Title: {car['title']}")
            print(f"Link: {car['link']}")
            print(f"Subtitle: {car['subtitle']}")
            print("-" * 40)
    else:
        print("No car information found")

if __name__ == "__main__":
    base_url = "https://lv.brcauto.eu/lietoti-auto"
    scraper = CarScraper(base_url)
    
    # Example usage
    params = {
        "city": "5",
        "search": "1",
        "makes": "31473"
    }
    
    car_info = scraper.scrape_cars(params)
    if car_info is not None:
        print_car_info(car_info)
    else:
        print("Failed to fetch the page")