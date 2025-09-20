from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

def test_screenshot():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.letskodeit.com/practice')
    sleep(3)

    hidden_button = driver.find_element(By.XPATH, "//input[@id='hide-textbox']")
    hidden_button.click()
    #Using Javascript
    displayed_textbox = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
    driver.execute_script("arguments[0].value = 'Hellow World'", displayed_textbox)
    sleep(5)
    print('Displayed text: ', displayed_textbox.get_attribute('value'))
    '''
    show_button = driver.find_element(By.XPATH, "//input[@id='show-textbox']")
    show_button.click()
    sleep(5)
    '''
    driver.quit()
