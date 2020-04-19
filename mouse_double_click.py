from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


def mouse_double_click():
    driver = webdriver.Chrome(executable_path='/Users/sandeepkumar/Documents/Selenium_Web_Automation/selenium_webdriver/chromedriver')
    driver.get("https://www.amazon.in")
    element = driver.find_element(By.LINK_TEXT, 'Best Sellers')
    action = ActionChains(driver)
    action.double_click(element).perform()
    time.sleep(3)
    driver.close()


if __name__== '__main__':
    mouse_double_click()

