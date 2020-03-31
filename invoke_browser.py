from selenium import webdriver
import time

def open_browser():
    driver = webdriver.Chrome(executable_path='/Users/sandeepkumar/Documents/Selenium_Web_Automation/chromedriver')
    driver.maximize_window()
    time.sleep(5)
    driver.close()


if __name__ == '__main__':
    open_browser()

