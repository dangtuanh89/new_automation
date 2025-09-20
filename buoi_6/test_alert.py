from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from time import sleep

def test_switch_window():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.letskodeit.com/practice")
    sleep(3)

    text_box = driver.find_element(By.XPATH, "//input[@placeholder = 'Enter Your Name']")
    text_box.send_keys("Selenium")
    confirm_btn = driver.find_element(By.XPATH, "//input[@id = 'confirmbtn']")
    confirm_btn.click()
    popup = driver.switch_to.alert
    print(popup.text)
    sleep(3)
    popup.accept()
    driver.switch_to.window(driver.window_handles[0])
    sleep(3)
    driver.quit()
