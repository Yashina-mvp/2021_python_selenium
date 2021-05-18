from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from common.webdriver_factory import get_driver
from module_05.sauce_func_lib.inventory import get_inventory
from module_05.sauce_func_lib.login import login, get_login_error
import pytest

LOGIN_DATA = [
    ('standard_user', 'secret_sauce'),
    ('performance_glitch_user', 'secret_sauce'),
    ('problem_user', 'secret_sauce'),
]


@pytest.mark.parametrize('user, password'.lOGIN_DATA)
def test_valid_user():
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 30)
    driver.get('https://www.saucedemo.com/')
    login(wait, 'standard_user', 'secret_sauce')
    items = get_inventory(wait)
    assert len(items) > 0, 'Inventory should be loaded'
    driver.close()


# assert items[0].title == 'Sauce Labs Backpack'
# assert items[1].title == 'Sauce Labs Bike Light'
# assert items[2].title == 'Sauce Labs Bolt T-Shirt'
# assert items[3].title == 'Sauce Labs Fleece Jacket'
# assert items[4].title == 'Sauce Labs Onesie'
# assert items[5].title == 'Test.allTheThings() T-Shirt (Red)'

_ERROR_MSG = 'Epic sadface: Username and password do not match any user in this service'


def test_invalid_user():
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 5)
    driver.get('https://www.saucedemo.com/')
    login(wait, 'standard_user', 'invalid_secret')
    error_msg = get_login_error(wait)
    assert error_msg is not None, 'Error message should be displayed for invalid login'
    assert error_msg == _ERROR_MSG, f'ERROR MESSAGE SHOULD BE {_ERROR_MSG}'
    with pytest.raises(TimeoutException):
        get_inventory(wait)
    driver.close()
