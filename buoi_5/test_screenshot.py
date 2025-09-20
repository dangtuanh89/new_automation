from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

def test_screenshot():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.letskodeit.com/practice')
    sleep(3)
    
    mouse_hover_element = driver.find_element(By.XPATH, "//button[@id='mousehover']")
    mouse_hover_element.screenshot("mouse_hover_element.png")
    driver.save_screenshot("screenshot.png")
    driver.quit()
    
    '''
    bmw_check = driver.find_element(By.XPATH, "//input[@id ='bmwcheck']")
    benz_check = driver.find_element(By.XPATH, "//input[@id ='benzcheck']")
    honda_check = driver.find_element(By.XPATH, "//input[@id ='hondacheck']")
    if not bmw_check.is_selected():
        bmw_check.click()
    if not benz_check.is_selected():
        benz_check.click()
    if not honda_check.is_selected():
        honda_check.click()
    sleep(5)
    driver.quit()    
    '''
    '''
    bmw_radio = driver.find_element(By.XPATH, "//input[@id ='bmwradio']")
    benz_radio = driver.find_element(By.XPATH, "//input[@id ='benzradio']")
    honda_radio = driver.find_element(By.XPATH, "//input[@id ='hondaradio']")
    bmw_radio.click()
    sleep(5)
    benz_radio.click()
    sleep(5)
    honda_radio.click()
    sleep(5)
    driver.quit()
    '''


