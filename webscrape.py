import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://sites.google.com/a/d219.org/ms-madigan/unit-4-polynomial-functions").read();
soup = BeautifulSoup(html, "html.parser");

table = soup.find("table", attrs={"border": "1"})
dates = [];


for row in table.findAll('tr'):
    col = row.findAll('td')
    if(col[0].string != "DATE" and col[0].string != None):
        dates.append(col[0].string)

print(dates)
