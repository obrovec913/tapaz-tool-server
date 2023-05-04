import pyautogui
from apars import savePars
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service(executable_path='chromedriver_win32 (3)\chromedriver.exe')
driver = webdriver.Chrome(service=s)
SEQUENCE = 'CC'
TAG = 'Постоянные собственные тайгены'
URL = 'https://ruscorpora.ru/results?search=CowBEmwKagoUCgtsYW5nX3NlYXJjaBIFCgNydXMSUgoJCgNsZXgSAgoACgoKBGZvcm0SAgoACiEKBWdyYW1tEhgKFihmYW1uIHwgcGVyc24gfCBwYXRybikKCQoDc2VtEgIKAAoLCgVmbGFncxICCgAqEAoICAAQChgyIDIgAEAFeAEyBwgFEgNlbmc6AQIwAQ=='
try:
    driver.maximize_window()
    driver.get(URL)
    time.sleep(20)
    savePars(driver.page_source, TAG)
    time.sleep(2)
    for i in range(117):
        driver.find_element(By.CSS_SELECTOR, '#rnc-spa > div.results-page > div:nth-child(1) > div:nth-child(2) > div > div > div > div > div.col-12.col-md-8.col-lg-7 > div > ul > li.ant-pagination-next > button').click()
        time.sleep(50)
        savePars(driver.page_source, TAG)
        time.sleep(4)
   

   
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
