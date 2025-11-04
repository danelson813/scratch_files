from bs4 import BeautifulSoup as bs
from playwright.sync_api import sync_playwright
from loguru import logger
from bs4 import MarkupResemblesLocatorWarning
import warnings
import os

warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)


def make_soup(url_: str, filepath: str) -> bs:
    logger.info("the url is {url_}")
    with sync_playwright() as p:
        # 1. Launch a new browser instance (Firefox in this case).
        # `headless=False` makes the browser visible for debugging.
        browser = p.firefox.launch(headless=True, slow_mo=50)

        # 2. Open a new page within the browser.
        page = browser.new_page()

        # 3. Navigate to a URL.
        page.goto(url_)
        save_soup(page.content(), filepath)
        soup = bs(page.content(), "html.parser")

    return soup


def save_soup(text: str, filepath: str) -> None:
    with open(filepath, "w") as f:
        f.write(str(text))


def get_soup(filepath) -> bs:
    with open(filepath, "r") as f:
        page = f.read()
        soup_ = bs(page, "html.parser")
    return soup_


def find_soup(url_: str, filepath: str) -> bs:
    if os.path.exists(filepath):
        soup_ = get_soup(filepath)
    else:
        soup_ = make_soup(url_, filepath)
    return soup_
