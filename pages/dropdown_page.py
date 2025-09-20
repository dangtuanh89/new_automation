from base.base_page import BasePage
from selenium.webdriver.common.by import By

class DropdownPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.dropdown_list = (By.XPATH, "//select[@id='dropdown']")
    
    def select_dropdown_list(self, select_value):
        dropdown_list = self.select_dropdown(self.dropdown_list, select_value)
    
    def get_selected_option(self):
        """Trả về text của option đang được chọn trong dropdown"""
        return self.get_selected_option_text(self.dropdown_list)