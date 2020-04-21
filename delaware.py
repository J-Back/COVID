from selenium import webdriver
import date
import main

def RunBrowser(driver):
    driver.get('https://dshs.maps.arcgis.com/apps/opsdashboard/index.html#/f2b22615feeb442aa2975900f8f2d4a1')

def Scraping(driver):
    featureList = driver.find_element_by_class_name('feature-list')

    for div in featureList.find_elements_by_class_name('list-item-content'):
        object = {
            'STATE': 'Delaware',
            'COUNTRY': div.find_elements_by_tag_name('p')[0].find_element_by_tag_name('span').text,
            'COUNT': div.find_elements_by_tag_name('p')[1].find_element_by_tag_name('span').text.split('positive')[0],
            'DEATHS': '0',
            'DATE': date.Time()
        }

        print(object)

        main.dataCoronavirus.append(object)

def Main():
    driver = webdriver.Chrome()

    RunBrowser(driver)
    driver.implicitly_wait(15)
    Scraping(driver)

if __name__ == '__main__':
    Main()