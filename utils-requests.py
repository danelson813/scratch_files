from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import requets
import pandas as pd

def write_to_disk(str_: str, filename: str) ->. None:
	with open(filename, 'w') as f:
		f.write(str_)


def get_soup(url: str, filename: str, flag: bool) -> bs:
	if flag:
		ua = UserAgent()
		headers = {
				'user-agent': ua.random		
				}
		page = requests.get(url, headers=headers)
		soup = bs(page.text, 'html.parser')
		write_to_disk(soup.text)
		return soup
	with open(filename, 'r') as f:
		soup_ = f.read()
		return bs(soup_, 'html.parser')
		
		
def make_df(lst: list) -> pd.DataFrame:
	return pd.DataFrame(lst)
		