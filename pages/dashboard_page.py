from base.base_page import BasePage
from selenium.webdriver.common.by import By

class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.dashboard = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
        self.recruitment = (By.XPATH, "//span[text()='Recruitment']")

    def confirm_navigate_to_dashboard_page(self):
        dashboard = self.get_element(self.dashboard)
        return dashboard.is_displayed()

    def navigate_to_recruitment_page(self):
        self.get_element(self.recruitment).click()


        
    