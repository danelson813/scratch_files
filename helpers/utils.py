# testing2/helpers/utils.py


from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import requests
import pandas as pd


def write_to_disk(str_: str, filename: str) -> None:
    with open(filename, "w") as f:
        f.write(str_)


def get_soup(url: str, filename: str, flag: bool) -> bs:
    if flag:
        ua = UserAgent()
        headers = {"user-agent": ua.random}

        page = requests.get(url, headers=headers)
        soup = bs(page.text, "html.parser")
        write_to_disk(soup)
        return soup
    with open(filename, "r") as f:
        soup_ = f.read()
        return bs(soup_, "html.parser")


def parse_page(soup: bs) -> list:
    movies = soup.find_all("ul")[11].find_all("li")
    results = []
    for movie in movies:
        result = {
            "rank": movie.find("h3").text.split(" ", 1)[0],
            "title": movie.find("h3").text.split(" ", 1)[1],
            "year": movie.select("span.sc-300a8231-7.eaXxft.cli-title-metadata-item")[
                0
            ].text,
            "runningtime": movie.select(
                "span.sc-300a8231-7.eaXxft.cli-title-metadata-item"
            )[1].text,
            "rating": movie.select("span.sc-300a8231-7.eaXxft.cli-title-metadata-item")[
                2
            ].text,
        }
        results.append(result)
    return results


def make_df(lst: list) -> pd.DataFrame:
    return pd.DataFrame(lst)
