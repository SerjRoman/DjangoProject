import os
from selenium import webdriver
import json
from selenium.webdriver.common.by import By
path_to_driver = os.path.join(os.path.abspath(__file__+'/..'),'chromedriver.exe')
driver = webdriver.Chrome(path_to_driver) 
driver.maximize_window()
driver.implicitly_wait(1)
list_url = []
with open('uri.txt','r') as file:
    list_url = file.read().split(',')
print(list_url)





domen_name = 'https://www.harlequin.com/shop/books/'
dict_xpaths = {
                'NAME':'//div[@class="book-detail-info-large"]/h1[@class="book-page__book-title"]',
                'PRICE':'//div[@class="format-button-list"]',
                'RATING':'//span[@class="rating-text"]',
                'IMAGE':'//img[@class="book-page-cover-image"]',
                'AUTHOR':'//div[@class="book-detail-info-large"]//child::div[1]',
                'DESCRIPTION':['//button[@class="book-page-back-of-book-read-toggle"]','//div[@class="book-page-back-of-book__content"]'],
                'DATE':'//div[@class="book-page-date"][2]',           
}
dict_db = {}

for url in list_url:
    dict_elements = {}
    url = domen_name+url
    site = driver.get(url)
    for key in dict_xpaths.keys():
        if key == 'IMAGE':
            element = driver.find_element(by=By.XPATH,value=dict_xpaths[key]).get_attribute('src')
        elif key == 'DESCRIPTION':
            button = driver.find_element(by=By.XPATH,value=dict_xpaths[key][0])
            driver.execute_script('arguments[0].click()', button)
            element = driver.find_element(by=By.XPATH,value=dict_xpaths[key][1]).text
            if '\n' in element:
                element = element.replace('\n',' ')
        else:
            element = driver.find_element(by=By.XPATH,value=dict_xpaths[key]).text
            if '\n' in element:
                element = element.replace('\n',' ')
            
        dict_elements[key] = element
    dict_db[url] = dict_elements
driver.quit()
print(dict_db)
with open('db.json','w') as file:
    json.dump(dict_db,file,indent=4)
print(dict_db)


