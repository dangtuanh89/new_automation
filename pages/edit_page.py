from selenium.webdriver.common.by import By
from base.base_page import BasePage

class EditPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.cancel_btn = (By.XPATH, "//button[text()=' Cancel ']")
        self.add_btn = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
    
    def click_cancel_btn(self):
        self.get_element(self.cancel_btn).click()

    def navigate_back_to_vacancy(self):
        return self.get_element(self.add_btn).is_displayed()
    
    
    
