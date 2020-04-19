from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

def alert():
    driver = webdriver.Chrome(executable_path='/Users/sandeepkumar/Documents/Selenium_Web_Automation/selenium_webdriver/chromedriver')
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    element = driver.find_element(By.LINK_TEXT, "Try Prime")
    act = ActionChains(driver)
    act.move_to_element(element).perform()
    time.sleep(2)
    driver.close()
    

if __name__== '__main__':
    alert()