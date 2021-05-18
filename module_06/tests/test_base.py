"""Base Test Class
Pytest Discovery: https://docs.pytest.org/en/stable/goodpractices.html#test-discovery


"""
from common.webdriver_factory import get_driver


class TestBase:
    """Base Test Class"""

    def setup_method(self):
        """Setup method"""
        self.driver = get_driver('chrome')

    def teardown_method(self):
        """Teardown method"""
        if self.driver:
            self.driver.close()
