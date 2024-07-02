from bs4 import BeautifulSoup
import requests


def fetch_soup(website_url):
    response = requests.get(website_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def output_decorator(func):
    def wrapper(*args, **kwargs):
        url = args[0]
        id = args[1]
        # Fetch the output from the decorated function
        output = func(*args, **kwargs)
        # Print the header only once
        if not wrapper.header_printed:
            print("NR | MODEL | YEAR | ENGINE | PRICE EUR | LINK")
            wrapper.header_printed = True
        print(output)
    wrapper.header_printed = False  # Flag to track if header is printed
    return wrapper


@output_decorator
def searcher(website_url, id) -> str:
    soup = fetch_soup(website_url)
    target_row = soup.find("tr", id=id)
    result = ""
    count = searcher.count
    if target_row:
        td_elements = target_row.find_all("td", class_="msga2-o pp6")
        link_element = target_row.find("a", class_="am")
        if link_element:
            car_link = "https://www.ss.com" + link_element.get("href")
        else:
            car_link = "Link not found"

        # Extract each text value and strip any extra spaces
        values = [td.get_text(strip=True) for td in td_elements]
        # Format the result with the correct spacing and euro sign
        result = f"{count}    {values[0]}     {values[1]}    {values[2]}     {values[3].strip('€')}  : {car_link}"
        searcher.count += 1
    else:
        result = f"Row with id='{id}' not found"

    return result


# Initialize the static variable count
searcher.count = 1

# Example usage
if __name__ == "__main__":
    url = 'https://www.ss.com/lv/transport/cars/bmw/3-series/'
    bmw_one = searcher(url, "tr_54757825")
    bmw_two = searcher(url, "tr_55126580")
    bmw_three = searcher(url, "tr_54908511")
    bmw_four = searcher(url, "tr_55126424")
    bmw_five = searcher(url, "tr_55126553")

