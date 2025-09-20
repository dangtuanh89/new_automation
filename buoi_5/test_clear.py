from selenium import webdriver
from time import sleep
import pytest
from selenium.webdriver.common.by import By

def test_clear():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    sleep(5)

    username = driver.find_element(By.XPATH, '//input[@name="username"]') 
    password = driver.find_element(By.XPATH, '//input[@name="password"]') 
    username.send_keys("Admin")
    password.send_keys("admin123")
    password.screenshot("inputed password.png")
    sleep(5)
    username.clear()
    password.clear()
    sleep(10)
    password.screenshot("cleared password.png")
    print("Password field: ", password.get_attribute('value'))
    driver.quit()
