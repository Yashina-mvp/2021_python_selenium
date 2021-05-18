import pytest
from selenium.webdriver.support.wait import WebDriverWait

from common.webdriver_factory import get_driver
from module_05.sauce_func_lib.login import login

ITEMS_LIST = [
    ('Sauce Labs Backpack', 'Sauce Labs Bike Light'),
    ('Sauce Labs Bolt T-shirt', 'Sauce Labs Fleece Jacket'),
    ('Sauce Labs Fleece Onesie', 'Test.allTheThings() T-Shirt (Red)'),
]


@pytest.mark.parametrize('user, password'.ITEMS_LIST)
def get_inventory():
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 30)
    driver.get('https://www.saucedemo.com/')
    login(wait, 'standard_user', 'secret_sauce')
    assert len(items) > 0, 'Inventory should be loaded'
    driver.close()