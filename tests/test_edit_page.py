from base.base_test import BaseTest
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.recruitment_page import RecruitmentPage
from pages.vacancy_page import VacancyPage
from pages.edit_page import EditPage

class TestEditPage(BaseTest):
    def test_edit_page(self):
        login_page = LoginPage(self.driver)
        login_page.login('Admin', 'admin123')
        
        dashboard_page = DashboardPage(self.driver)
        assert dashboard_page.confirm_navigate_to_dashboard_page(), "Navigated to Dashboard page failed"
        print('Navigated to Dashboard page successfully')
        
        dashboard_page.navigate_to_recruitment_page()

        recruitement_page = RecruitmentPage(self.driver)
        assert recruitement_page.confirm_navigate_to_recruitment_page(), "Navigate to Recruitment page failed"
        print('Navigated to Recruitment page sucessfully')

        recruitement_page.navigate_to_vacancy()
        
        vacancy_page = VacancyPage(self.driver)
        assert vacancy_page.confirm_navigate_to_vacancy_page(), "Navigate to Vacancy page failed"
        print('Navigated to vacancy page successfully')

        vacancy_page.click_add_btn()
        assert vacancy_page.confirm_navigate_to_edit_page(), "Click on Add button failed"
        print('Click on Add button successfully')
        
        vacancy_page.input_vacancy_data("Automation Tester", "Automation Test Is Running", "2")
        assert vacancy_page.confirm_navigate_to_edit_page(), "Navigate to edit page failed"
        print('Navigate to edit page successfully')

        edit_page = EditPage(self.driver)
        edit_page.click_cancel_btn()
        assert edit_page.navigate_back_to_vacancy(), "Failed to navigate back to Vacancies page"
        print("Navigate back to Vacancies page successfully")
    
