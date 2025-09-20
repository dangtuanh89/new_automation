from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return element
    
    def get_elements(self, locator):
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))
        return elements
    
    def select_dropdown(self, locator, select_value):
        select = Select(WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)))
        select.select_by_visible_text(select_value)
    
    def get_selected_option_text(self, locator):
        # Return text of option is being selected in dropdown
        select = Select(WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)))
        return select.first_selected_option.text
    
    def js_click(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)