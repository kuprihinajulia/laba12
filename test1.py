from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

 # Получаем в переменную browser указатель на браузер
browser=webdriver.Edge('./msedgedriver')
browser.get('https://trovo.live/')

button=browser.find_element(by=By.XPATH, value='//*[@id="__layout"]/div/nav/div[3]/div[4]/button')
button.click()
time.sleep(10)

username=browser.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[2]/div[3]/div[1]/div[1]/div/input')
username.send_keys('EWTUHXJ')
time.sleep(2)

password=browser.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[2]/div[3]/div[1]/div[3]/div/input')
password.send_keys('JGHhfj24')
time.sleep(2)


button=browser.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[2]/div[3]/div[1]/button')
button.click()
time.sleep(4)

#Закрываем браузер
browser.close()
