from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import date
import main

def RunBrowser(driver):
    driver.get('https://cvprovider.nmhealth.org/public-dashboard.html')

def Scraping(driver):
    select = Select(driver.find_element_by_id('counties-select').find_element_by_tag_name('Select'))
    listOptions = select.options

    del listOptions[:2]

    for obj in listOptions:
        value = obj.get_attribute('value')

        select.select_by_value(value)
        time.sleep(1)

        information = driver.find_element_by_xpath(f'//div[@data-county-id="{value}"]')

        object = {
            'STATE': 'New Mexico', 
            'COUNTRY': information.find_elements_by_tag_name('div')[0].text,
            'COUNT': information.find_elements_by_tag_name('div')[1].text.split(':')[1],
            'DEATHS': information.find_elements_by_tag_name('div')[2].text.split(':')[1],
            'DATE': date.Time()
        }

        main.dataCoronavirus.append(object)

def Main():
    driver = webdriver.Chrome()

    RunBrowser(driver)
    time.sleep(5)
    Scraping(driver)

if __name__ == '__main__':
    Main()