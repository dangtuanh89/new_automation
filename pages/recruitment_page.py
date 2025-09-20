from base.base_test import BaseTest
from selenium.webdriver.common.by import By
from base.base_page import BasePage

class RecruitmentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.vacancies = (By.XPATH, "//a[text()='Vacancies']")   
    
    def confirm_navigate_to_recruitment_page(self):
        vacancies = self.get_element(self.vacancies)
        return vacancies.is_displayed()
    
    def navigate_to_vacancy(self):
        self.get_element(self.vacancies).click()


    