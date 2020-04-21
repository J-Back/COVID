import requests
import pandas as pd
import date
import main
from io import StringIO

def Scraping(dataFrame):
    for obj in dataFrame['County_1']:
        tempData = dataFrame[dataFrame['County_1'] == obj]

        object = {
            'STATE': 'Florida',
            'COUNTRY': tempData['County_1'].iloc[0],
            'COUNT': tempData['CasesAll'].iloc[0],
            'DEATHS': tempData['Deaths'].iloc[0],
            'DATE': date.Time()
        }

        main.dataCoronavirus.append(object)

def Main():
    dataFrame = pd.read_csv(StringIO(requests.get('http://opendata.arcgis.com/agol/arcgis/a7887f1940b34bf5a02c6f7f27a5cb2c/0.csv?').text))[['County_1', 'CasesAll', 'Deaths']]

    Scraping(dataFrame)

if __name__ == '__main__':
    Main()