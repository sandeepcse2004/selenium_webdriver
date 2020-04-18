from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def navigation():
    driver = webdriver.Chrome(executable_path='/Users/sandeepkumar/Documents/Selenium_Web_Automation/selenium_webdriver/chromedriver')
    driver.get("https:/www.amazon.in")
    driver.maximize_window()
    driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('iphone')
    driver.find_element_by_id('twotabsearchtextbox').send_keys(Keys.RETURN)
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.forward()
    driver.close()

if __name__== '__main__':
    navigation()