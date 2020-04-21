import requests
import main
import date
from bs4 import BeautifulSoup

def Scraping(page):
    table = page.find_all('div', class_ = 'wp-block-group')

    del table[:4]
    del table[-1]

    for obj in table:
        object = {
            'STATE': 'Hawaii',
            'COUNTRY': obj.find('table', class_ = 'has-fixed-layout').find('thead').find_all('th')[0].text,
            'COUNT': obj.find('table', class_ = 'has-fixed-layout').find('tbody').find_all('tr')[0].find_all('td')[1].text.split(' ')[0],
            'DEATHS': obj.find('table', class_ = 'has-fixed-layout').find('tbody').find_all('tr')[-1].find_all('td')[1].text,
            'DATE': date.Time()
        }

        main.dataCoronavirus.append(object)

def Main():
    page = BeautifulSoup(requests.get('https://health.hawaii.gov/coronavirusdisease2019/what-you-should-know/current-situation-in-hawaii/').text, 'html.parser')

    Scraping(page)

if __name__ == '__main__':
    Main()