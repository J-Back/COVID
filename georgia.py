import requests
import date
import main
from bs4 import BeautifulSoup

def Scraping(page):
    table = page.find_all('table')[9]
    tr = table.find_all('tr')

    del tr[0]

    for obj in tr:
        td = obj.find_all('td')

        if len(td) == 3:
            object = {
                'STATE': 'Georgia',
                'COUNTRY': td[0].text,
                'COUNT': td[1].text,
                'DEATHS': td[2].text,
                'DATE': date.Time()
            }
            
            main.dataCoronavirus.append(object)

        else:
            continue

def Main():
    page = BeautifulSoup(requests.get('https://d20s4vd27d0hk0.cloudfront.net/?initialWidth=746&childId=covid19dashdph&parentTitle=COVID-19%20Daily%20Status%20Report%20%7C%20Georgia%20Department%20of%20Public%20Health&parentUrl=https%3A%2F%2Fdph.georgia.gov%2Fcovid-19-daily-status-report').text, 'html.parser')

    Scraping(page)

if __name__ == '__main__':
    Main()