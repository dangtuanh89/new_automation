import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.config_reader import ConfigReader
class BaseTest:
    @pytest.fixture(scope='class', autouse= True)
    def setup_driver(self, request):
        chrome_options = webdriver.ChromeOptions()
        # Chrome options cho headless mode trên Ubuntu/Linux
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        
        base_url = ConfigReader.get_base_url()
        if base_url:
            self.driver.get(base_url)
            
        request.cls.driver = self.driver
        yield
        self.driver.quit()