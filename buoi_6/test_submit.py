from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from time import sleep

def test_submit():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://the-internet.herokuapp.com/login")
    sleep(5)
    username = driver.find_element(By.XPATH, "//input[@id='username']")
    username.send_keys("tomsmith")
    password = driver.find_element(By.XPATH, "//input[@id='password']")
    password.send_keys("SuperSecretPassword!")
    password.submit()
    driver.quit()


