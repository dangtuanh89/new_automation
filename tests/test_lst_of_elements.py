from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_test import BaseTest

class TestLstOfElements(BaseTest):
    def test_lst_of_elements(self):
        wait = WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.XPATH, "//input")))
        elements = self.driver.find_elements(By.XPATH, "//input")
        print(f'Number of input elemnts found: {len(elements)}')
        for element in elements:
            print(f"Element placeholder: {element.get_attribute('placeholder')}")
        self.driver.quit()

