from selenium import webdriver
import date
import time
import main

def RunBrowser(driver):
    driver.get('https://maps.arcgis.com/apps/opsdashboard/index.html#/ec4bffd48f7e495182226eee7962b422')

def Scraping(driver):
    list_item_content = driver.find_elements_by_class_name('list-item-content')

    del list_item_content[0]
    del list_item_content[-1]

    for obj in list_item_content:
        object = {
            'STATE': 'New Jersey',
            'COUNTRY': obj.find_elements_by_tag_name('p')[0].find_element_by_tag_name('strong').text.split(':')[0],
            'COUNT': obj.find_elements_by_tag_name('p')[1].find_element_by_tag_name('strong').text,
            'DEATHS': obj.find_elements_by_tag_name('p')[2].find_element_by_tag_name('strong').text,
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