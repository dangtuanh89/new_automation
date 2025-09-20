from selenium import webdriver
from time import sleep
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_auto_complete():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com/")
    sleep(5)
    
    search_box = driver.find_element(By.XPATH, "//textarea[@name='q']")
    search_box.send_keys('Selenium')
    search_box.send_keys(Keys.ARROW_DOWN)
    sleep(2)
    search_box.send_keys(Keys.ARROW_DOWN)
    sleep(2)
    search_box.send_keys(Keys.ARROW_DOWN)
    sleep(2)
    search_box.send_keys(Keys.ENTER)
    '''
    google_logo = driver.find_element(By.XPATH, "//div[@class='o3j99 LLD4me yr19Zb LS8OJ']")
    google_logo.screenshot("google_logo.png")
    driver.quit()
    '''


