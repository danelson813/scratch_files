from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
from datetime import datetime
import time
import os
import re
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException


service = Service("path to Chromedriver download")
options = Options()
options.add_argument("--incognito")
options.add_argument("start_maximized")
options.add_argument("--headless")

driver = webdriver.Chrome(service=service, options=options)
