from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
'''
def test_mouse_hover():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/menu")
    sleep(3)

    sub_menu_2 = driver.find_element(By.XPATH, "//a[text()='Main Item 2']")
    sleep(3)

    actions = ActionChains(driver)
    actions.move_to_element(sub_menu_2)
    actions.perform()
    sleep(3)
    driver.quit()
'''
def test_mouse_hover():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.letskodeit.com/practice")
    sleep(3)

    mouse_hover = driver.find_element(By.XPATH, "//button[@id = 'mousehover']")
    sleep(3)

    actions = ActionChains(driver)
    actions.move_to_element(mouse_hover)
    actions.perform()
    driver.quit()