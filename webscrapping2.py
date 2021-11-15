from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(url)
soup = bs(page.text, 'html.parser')
star_table = soup.find_all('table')

temp_list = []
table_rows = star_table[7].find_all('tr')