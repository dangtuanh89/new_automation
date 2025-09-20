from base.base_test import BaseTest
from pages.dropdown_page import DropdownPage

class TestDropdownList(BaseTest):
    def test_dropdown_option1(self):
        dropdown_page = DropdownPage(self.driver)
        dropdown_page.select_dropdown_list('Option 1')
        assert dropdown_page.get_selected_option() == 'Option 1', "Failed"
        print(dropdown_page.get_selected_option())

    def test_dropdown_option2(self):
        dropdown_page = DropdownPage(self.driver)
        dropdown_page.select_dropdown_list('Option 2')
        assert dropdown_page.get_selected_option() == 'Option 2', "Failed"
        print(dropdown_page.get_selected_option())