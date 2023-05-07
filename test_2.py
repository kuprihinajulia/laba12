from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver import Keys 
import time 

 # Получаем в переменную browser указатель на браузер
browser=webdriver.Edge('./msedgedriver')

# Переходим на страницу, на которой находится форма для авторизации
browser.get('https://trovo.live/')
 
time.sleep(2) 
ggg = browser.find_element(by=By.LINK_TEXT, value='Актуальное') 
ggg.click()
time.sleep(2) 

#Закрываем браузер
browser.close()
