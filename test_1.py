from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

 # Получаем в переменную browser указатель на браузер
browser=webdriver.Edge('./msedgedriver')

# Переходим на страницу, на которой находится форма для авторизации
browser.get('https://trovo.live/')
 
search=browser.find_element(by=By.CLASS_NAME, value='search-content > .search-input') 
time.sleep(1) 
search.send_keys('игры') 
time.sleep(2) 
search.send_keys(Keys.ENTER) 
time.sleep(3)

#Закрываем браузер
browser.close()