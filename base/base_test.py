import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
class BaseTest:
    @pytest.fixture(scope='class', autouse= True)
    def setup_driver(self, request):
        chrome_options = webdriver.ChromeOptions()
        # Chrome options cho headless mode trên Ubuntu/Linux
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        request.cls.driver = self.driver
        yield
        self.driver.quit()