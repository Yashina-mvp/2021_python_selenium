"""Base Test Class"""
from selenium.webdriver.support.wait import WebDriverWait
from common.webdriver_factory import  get_driver


class TestBase:
    """Test base"""

    def setup_method(self):
        """set up method"""
        print('Method setup')
        self.driver = get_driver('chrome')
        self.wait = WebDriverWait(self.driver, 3)
        self.driver.get('https://www.saucedemo.com/')

    def teardown_method(self):
        """Teardown method"""
        print('method teardown')
        if self.driver:
            self.driver.close()
