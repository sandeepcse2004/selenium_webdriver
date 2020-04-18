from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def checkBox():
    driver  = webdriver.Chrome(executable_path='/Users/sandeepkumar/Documents/Selenium_Web_Automation/selenium_webdriver/chromedriver')
    driver.get('https://www.oyorooms.com/hotels-in-goa/')
    driver.maximize_window()
    driver.find_element(By.ID, 'android-app-luxury-collection').click()
    time.sleep(5)

    

if __name__== '__main__':
    checkBox()