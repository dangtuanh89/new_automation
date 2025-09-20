from base.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username = (By.XPATH, "//input[@name='username']")
        self.password = (By.XPATH, "//input[@name='password']")
        self.login_btn = (By.XPATH, "//button[@type='submit']")

    def login(self, username_value, password_value):
        username = self.get_element(self.username).send_keys(username_value)
        password = self.get_element(self.password).send_keys(password_value)
        login_btn = self.get_element(self.login_btn).click()
        