from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


def mouse_right_click():
    driver = webdriver.Chrome(executable_path='/Users/sandeepkumar/Documents/Selenium_Web_Automation/selenium_webdriver/chromedriver')
    driver.get("https://www.amazon.in")
    driver.maximize_window()
    element = driver.find_element(By.LINK_TEXT, 'Customer Service')
    action = ActionChains(driver)
    action.context_click(element).perform()
    time.sleep(4)


if __name__ == '__main__':
    mouse_right_click()

