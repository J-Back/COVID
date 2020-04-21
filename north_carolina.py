import requests
import date
import pandas as pd
import main
from bs4 import BeautifulSoup

def Scraping(page):
    tr = page.find_all('section', class_ = 'tab-main')[1].find_all('tr')

    del tr[0]

    for td in tr:
        object = {
            'STATE': 'North Carolina',
            'COUNTRY': td.find_all('td')[0].text,
            'COUNT': td.find_all('td')[1].text,
            'DEATHS': td.find_all('td')[2].text,
            'DATE': date.Time()
        }

        main.dataCoronavirus.append(object)

    data = pd.DataFrame(data = main.dataCoronavirus)
    data.to_csv('output.csv')

def Main():
    page = BeautifulSoup(requests.get('https://www.ncdhhs.gov/divisions/public-health/covid19/covid-19-nc-case-count#by-counties').text, 'html.parser')

    Scraping(page)

if __name__ == '__main__':
    Main()