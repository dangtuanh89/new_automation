from selenium import webdriver
from time import sleep
import pytest
from selenium.webdriver.common.by import By

def test_checkbox():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    sleep(5)
    checkbox_1 = driver.find_element(By.XPATH, "//*[@id='checkboxes']/input[1]")
    checkbox_2 = driver.find_element(By.XPATH, "//*[@id='checkboxes']/input[2]")
    sleep(3)
    if not checkbox_1.is_selected():
        checkbox_1.click()
    if not checkbox_2.is_selected():
        checkbox_2.click()    
    sleep(5)
    driver.quit()