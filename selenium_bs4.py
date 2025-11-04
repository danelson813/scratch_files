# whiskey_river/app.py
import pandas as pd
from selenium import webdriver
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from time import sleep


url = "https://www.thewhiskyexchange.com/new-products/standard-whisky#nav"
base = "https://www.thewhiskyexchange.com"

def get_soup(url_: str) -> BeautifulSoup:
    options = Options()
    options.add_argument("--headless")
    ua = UserAgent()
    user_agent = ua.random
    options.add_argument(f"user-agent:{user_agent}")
    with webdriver.Firefox(
        service=Service("/Users/geckodriver"), options=options) as driver:
        driver.get(url_)
        sleep(2)
        driver.maximize_window()
        driver.save_screenshot("data/homepage.png")
        soup_ = BeautifulSoup(driver.page_source, "html.parser")

        return soup_


if __name__ == '__main__':
    soup = get_soup(url)
    bottles = soup.find_all('li', class_='product-grid__item')
    results = []
    print(len(bottles))
    for bottle in bottles:
        result = {
        'title': bottle.find("p", class_='product-card__name').text,
        'price': bottle.find('p', class_='product-card__price').text,
        'link': base+bottle.find('a')['href']
        }
        print(result)
        results.append(result)
    df = pd.DataFrame(results)
    df.to_csv('data/results.csv', index=False)
