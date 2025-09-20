from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.recruitment_page import RecruitmentPage

class TestRecruitmentPage(BaseTest):
    def test_navigate_to_recruitement_page(self):
        login_page = LoginPage(self.driver)
        login_page.login('Admin', 'admin123')
        
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.navigate_to_recruitment_page()

        recruitement_page = RecruitmentPage(self.driver)
        assert recruitement_page.confirm_navigate_to_recruitment_page(), "Navigated to Recruitment page failed"
        print('Navigated to Recruitment page successfully')