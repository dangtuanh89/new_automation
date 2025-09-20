from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

def test_drag_drop():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://demo.guru99.com/test/drag_drop.html")
    sleep(3)
    drag_block_5000 = driver.find_element(By.XPATH, "//*[@id = 'fourth']")
    drop_amount = driver.find_element(By.XPATH, "//*[@id='amt7']/li")

    ActionChains(driver).drag_and_drop(drag_block_5000, drop_amount).perform()
    sleep(5)
    driver.quit()
