from selenium import webdriver
from time import sleep
import pytest
from selenium.webdriver.common.by import By

def test_radio_button():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_radio")
    sleep(5)

    #Do toàn bộ phần HTML có radio buttons đều nằm bên trong iframeResult
    driver.switch_to.frame("iframeResult")
    #Sau khi làm việc xong, nếu cần thao tác với phần tử bên ngoài iframe (Khi bạn muốn quay lại trang chính), dùng:driver.switch_to.default_content()

    html = driver.find_element(By.XPATH, "//input[@id='html']")
    css = driver.find_element(By.XPATH, "//input[@id='css']")
    javascript = driver.find_element(By.XPATH, "//input[@id='javascript']")
    html.click()
    sleep(5)
    css.click()
    sleep(5)
    javascript.click()
    sleep(5)
    driver.quit()