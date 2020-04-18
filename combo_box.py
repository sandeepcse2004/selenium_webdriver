from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def comboBox():
    driver  = webdriver.Chrome(executable_path='/Users/sandeepkumar/Documents/Selenium_Web_Automation/selenium_webdriver/chromedriver')
    driver.get('https://www.facebook.com/')
    selected = Select(driver.find_element(By.ID, 'day'))
    selected.select_by_index(4)
    time.sleep(1)
    selected.select_by_value('18')
    time.sleep(1)
    selected.select_by_visible_text('Day')
    time.sleep(1)
    driver.close()

    
if __name__== '__main__':
    comboBox()