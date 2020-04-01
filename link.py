from selenium import webdriver
import time

def link():
    """
        This method is responsible to click on the link of amazon webpage.
        Xpath has been used to locate the element.
    """
    driver = webdriver.Chrome(executable_path='D:/02_VSCode_Python/Selenium_Automation/chromedriver')
    driver.get("https:/www.amazon.in")
    driver.maximize_window()
    time.sleep(1)
    driver.find_element_by_xpath("//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers']").click()
    time.sleep(3)
    driver.close()


if __name__ == '__main__':
    link()