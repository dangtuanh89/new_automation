from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from time import sleep

def test_switch_window():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.letskodeit.com/practice")
    sleep(3)
    
    open_window = driver.find_element(By.XPATH, "//button[@id='openwindow']")
    open_window.click()
    count_window = len(driver.window_handles)
    print("Number of window:", count_window)
    driver.switch_to.window(driver.window_handles[1])
    driver.maximize_window()
    sleep(3)
    all_courses = driver.find_element(By.XPATH, "//h1[@class='dynamic-heading margin-bottom-20']")
    assert "All Courses" in all_courses.text, "Failed"
    print('Switch to new window sucessfully')
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    sleep(3)
    driver.quit()
    
