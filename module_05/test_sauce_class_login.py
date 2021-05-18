import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from common.webdriver_factory import get_driver
from module_05.sauce_func_lib.inventory import get_inventory
from module_05.sauce_func_lib.login import get_login_error, login
from module_05.sauce_func_lib.TestBase import TestBase

class TestLogin(TestBase):
    _ERROR_MSG = 'Epic sadface: Username and password do not match any user in this service'

    def setup_method(self):
        """setup method"""
        print('Method setup')
        self.driver = get_driver('chrome')
        self.wait = WebDriverWait(self.driver, 3)
        self.driver.get('https://www.saucedemo.com/')

    def teardown_method(self):
        """Teardown method"""
        print('Method Teardown')
        if self.driver:
            self.driver.close()

    def test_login(self):
        login(self.wait, 'standard_user', 'secret_sauce')
        items = get_inventory(self.wait)
        assert len(items) > 0, 'Inventory should be loaded'

    def test_invalid_login(self):
        login(self.wait, 'standard_user', 'invalid_secret')
        error_msg = get_login_error(self.wait)
        assert error_msg is not None, 'Error message should be displayed for invalid login'
        assert error_msg == TestBase._ERROR_MSG, f'ERROR MESSAGE SHOULD BE {TestBase._ERROR_MSG}'
        with pytest.raises(TimeoutException):
            get_inventory(self.wait)
