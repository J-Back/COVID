import requests
import date
import main
from bs4 import BeautifulSoup

def Scraping(page):
    tr = page.find('table', class_ = 'county-table').find_all('tr')

    del tr[0]
    del tr[-1]

    for obj in tr:
        object = {
            'STATE': 'New Hampshire',
            'COUNTRY': obj.find_all('td')[0].text,
            'COUNT': obj.find_all('td')[1].text,
            'DEATHS': '0',
            'DATE': date.Time()
        }

        main.dataCoronavirus.append(object)

def Main():
    page = BeautifulSoup(requests.get('https://www.nh.gov/covid19/').text, 'html.parser')

    Scraping(page)

if __name__ == '__main__':
    Main()