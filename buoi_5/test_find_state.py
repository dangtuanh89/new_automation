from selenium import webdriver
from time import sleep
import pytest
from selenium.webdriver.common.by import By

def test_is_displayed():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    sleep(5)

    username = driver.find_element(By.XPATH, '//input[@name="username"]') 
    password = driver.find_element(By.XPATH, '//input[@name="password"]')
    print(username.is_displayed())
    print(password.is_displayed())
    driver.quit()

