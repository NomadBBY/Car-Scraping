from bs4 import BeautifulSoup
import requests

def fetch_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def searcher(url, id) -> str:
    soup = fetch_soup(url)
    target_row = soup.find("tr", id=id)
    result = ""
    count = 1  # Initialize a counter
    if target_row:
        td_elements = target_row.find_all("td", class_="msga2-o pp6")
        combined_text = " | ".join(td.get_text(strip=True) for td in td_elements)
        result = f"{count} | {combined_text}"
    else:
        result = f"Row with id='{id}' not found"

    return result

# Example usage
url = 'https://www.ss.com/lv/transport/cars/bmw/3-series/'
output = searcher(url, "tr_54757825")
print("NR | MODEL | YEAR | ENGINE | PRICE EUR")
print(output)
