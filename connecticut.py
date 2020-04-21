import requests
import pandas as pd
import main
import date
import datetime
from io import StringIO

def DateGeneration():
    now = datetime.datetime.now()

    return f'{now.year}-{now.month}-{now.day - 1}'

def Scraping(dataFrame):
    for obj in dataFrame['county']:
        tempData = dataFrame[dataFrame['county'] == obj]

        object = {
            'STATE': 'Connecticut',
            'COUNTRY': obj,
            'COUNT': tempData['cases'][0],
            'DEATHS': tempData['deaths'][0],
            'DATE': date.Time()
        }

        main.dataCoronavirus.append(object)

def Main():
    dataFrame = pd.read_csv(StringIO(requests.get('https://data.ct.gov/resource/bfnu-rgqt.csv').text),
                       index_col = 'dateupdated', parse_dates = True)

    if len(dataFrame[dataFrame.index == date.Time()]) == 0:
        dataFrame = dataFrame[dataFrame.index == DateGeneration()]
    else:
        dataFrame = dataFrame[dataFrame.index == date.Time()]

    Scraping(dataFrame)
 
if __name__ == '__main__':
    Main()

