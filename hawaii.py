import requests
import main
import date
from bs4 import BeautifulSoup

def Scraping(page):
    td = page.find('table').find_all('td')

    HAWAII = {
        'STATE': 'Hawaii',
        'COUNTY': 'Hawaii County',
        'COUNT': td[21].text,
        'DEATHS': td[27].text,
        'DATE': date.Time()
    }

    HONOLULU = {
        'STATE': 'Hawaii',
        'COUNTY': 'Honolulu County',
        'COUNT': td[33].text,
        'DEATHS': td[39].text,
        'DATE': date.Time()
    }

    KAUAI = {
        'STATE': 'Hawaii',
        'COUNTY': 'Kauai County',
        'COUNT': td[45].text,
        'DEATHS': td[51].text,
        'DATE': date.Time()
    }

    MAUI = {
        'STATE': 'Hawaii',
        'COUNTY': 'Maui County',
        'COUNT': td[57].text,
        'DEATHS': td[63].text,
        'DATE': date.Time()
    }

    main.DATA.append(HAWAII)
    main.DATA.append(HONOLULU)
    main.DATA.append(KAUAI)
    main.DATA.append(MAUI)

def Main():
    page = BeautifulSoup(requests.get('https://health.hawaii.gov/coronavirusdisease2019/what-you-should-know/current-situation-in-hawaii/').text, 'html.parser')

    Scraping(page)

if __name__ == '__main__':
    Main()