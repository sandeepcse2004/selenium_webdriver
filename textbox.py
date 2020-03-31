from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def textbox():
    driver = webdriver.Chrome(executable_path='/Users/sandeepkumar/Documents/Selenium_Web_Automation/selenium_webdriver/chromedriver')
    driver.get("https:/www.amazon.in")
    driver.maximize_window()
    driver.find_element_by_id('twotabsearchtextbox').send_keys('Redmi')
    driver.find_element_by_id('twotabsearchtextbox').send_keys(Keys.RETURN)
    time.sleep(5)
    driver.close()

if __name__== '__main__':
    textbox()