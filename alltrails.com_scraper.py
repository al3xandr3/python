# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 22:41:07 2020

@author: amatos
"""

# https://github.com/oschow/take-a-hike/blob/master/AllTrails/scrape_clean/scrape_ratings.py

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
#from pymongo import MongoClient
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json
from pandas import json_normalize
import pickle


def get_all_hikes(browser):
    browser.get('https://www.alltrails.com/us/washington?ref=search')
    counter = 120
    while counter > 0:
        try:
            load_more_hikes = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CLASS_NAME,"styles-module__button___1nuva")))
            load_more_hikes.click()
            time.sleep(7)
        except:
            break
        counter = counter - 1
        print(counter)
    soup = BeautifulSoup(browser.page_source)
    return soup


def parse_meta_data(hike_soup):
    
    try:
        
        header = hike_soup.find('div', id='title-and-menu-box')
    
        k = header.find(attrs={"data-react-props": True} )
        
        output = k.get('data-react-props')
        
        j1 = json.loads(output)
        
        df = json_normalize(j1)
    
        df = df.drop(['photos', "exploreFlag", 'isVerified', 'mobileBrowser', 'isFavorite', 'context.currentUser', 'context.adminUser', 'context.proUser', 'context.mobileBrowser', 'context.tabletBrowser', 'context.displayMetric', 'context.languageRegionCode'], axis=1)
    
        with open("C:\\Users\\amatos\\Google Drive\\my\\projects\\python\\trails.csv", 'a') as f:
            df.to_csv(f, mode='a', header=f.tell()==0)
    
    except:
        print("> FAILED")


def create_db(soup, browser):
    hikes = soup.select('.styles-module__link___12BPT')
    for h in hikes:
        #h = hike.findChild('a')
        #if h == None:
        #    continue
        hike_url = 'http://www.alltrails.com' + h['href']
        print(hike_url)
        browser.get(hike_url)
        soup = BeautifulSoup(browser.page_source)
        parse_meta_data(soup)
       


if __name__ == '__main__':

    browser  = webdriver.Chrome(ChromeDriverManager().install())
 
    soup = get_all_hikes(browser)

    create_db(soup, browser)    
