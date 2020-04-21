from selenium import webdriver
import date
import time
import main

def RunBrowser(driver):
    driver.get('https://alpublichealth.maps.arcgis.com/apps/opsdashboard/index.html#/6d2771faa9da4a2786a509d82c8cf0f7')

def Scraping(driver):
    featureList = driver.find_element_by_class_name('feature-list')

    for div in featureList.find_elements_by_class_name('list-item-content'):
        object = {
            'STATE': 'Alabama',
            'COUNTRY': div.find_elements_by_tag_name('p')[0].find_elements_by_tag_name('span')[0].text.split(':')[0],
            'COUNT':  div.find_elements_by_tag_name('p')[0].find_elements_by_tag_name('span')[1].text,
            'DEATHS': div.find_elements_by_tag_name('p')[1].find_elements_by_tag_name('span')[3].text,
            'DATE': date.Time()
        }

        main.dataCoronavirus.append(object)
           
def Main():
    driver = webdriver.Chrome()

    RunBrowser(driver)
    time.sleep(15)
    Scraping(driver)

if __name__ == '__main__':
    Main()