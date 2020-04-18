from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def radioButton():
    driver  = webdriver.Chrome(executable_path='/Users/sandeepkumar/Documents/Selenium_Web_Automation/selenium_webdriver/chromedriver')
    driver.get('https://www.facebook.com/')
    driver.find_element(By.ID, 'u_0_6').click()
    time.sleep(1)
    driver.find_element(By.ID, 'u_0_7').click()
    

if __name__== '__main__':
    radioButton()