from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import pytest
from utils.config_reader import ConfigReader
class TestLogin(BaseTest):
    @pytest.mark.smoke
    def test_login(self):
        
        login_page = LoginPage(self.driver)
        login_page.login(ConfigReader.get_username(), ConfigReader.get_password())
        
        dashboard_page = DashboardPage(self.driver)
        assert dashboard_page.confirm_navigate_to_dashboard_page(), "Navigated to Dashboard page failed"
        print('Navigated to Dashboard page successfully')
    
    