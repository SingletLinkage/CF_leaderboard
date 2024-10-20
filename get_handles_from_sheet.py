import typing
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrapeDataFromSpreadsheet(link: str) -> typing.List[typing.List[str]]:
    html = requests.get(link).text
    soup = BeautifulSoup(html, 'lxml')
    salas_cine = soup.find_all('table')[0]
    rows = [[td.text for td in row.find_all("td")] for row in salas_cine.find_all('tr')]
    return rows


link = 'https://docs.google.com/spreadsheets/d/1pi32lljISYr9mETR9SePL_poXjyHJ_Q2zMsIc8zNQAw/edit?usp=sharing'
df_list = pd.read_html(link)

print(df_list[0])