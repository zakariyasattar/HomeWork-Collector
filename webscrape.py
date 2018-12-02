import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import calendar
import csv

def formatDate(str):
    finalString = ""

    months = ["", "Jan", "Feb", "Mar", "May", "Apr", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    days = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]

    indexInString = str.find("/")
    val = str[:indexInString]
    month = months[int(val)]

    currentNumber = str[indexInString+1:]
    if(currentNumber[0] == "0"):
        currentDay = days[datetime.datetime.today().weekday()];
        finalString = currentDay + ", " + month + " " + str[indexInString+2:]
    else:
        currentDay = days[datetime.datetime.today().weekday()];
        finalString = currentDay + ", " + month + " " + str[indexInString+1:]
    return finalString


now = datetime.datetime.now()
dates = []
href = []
finalHw = []

html = urlopen("https://sites.google.com/a/d219.org/ms-madigan/unit-4-polynomial-functions").read();
soup = BeautifulSoup(html, "html.parser");
table = soup.find("table", attrs={"border": "1"})


counter = 0
for row in table.findAll('tr'):
    counter+=1
    col = row.findAll('td')
    val = col[0].string

    if(counter > 1 and val != None):
        dates.append(val)

    for x in col[2].findAll('a'):
        row = []
        row.append(val.replace("\xa0", ""))
        for y in col[2].findAll('a'):
            row.append(y)
        href.append(row)

    for d in dates:
        # today = formatDate(now.strftime("%m/%d"))
        # today = "Tues, Nov 27"
        today = "Wed, Nov 28"

        if(d == today or d[1:] == today):
            for link in href:
                finalHw.append([link[0], link[len(link) - 1]])
            for date in finalHw:
                if(date[0] == d or date[0] == d[1:]):
                    print("today's homework for math is: " + str(date[1]))
