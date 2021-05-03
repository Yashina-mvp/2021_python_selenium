from selenium.webdriver.support.wait import WebDriverWait
from common.webdriver_factory import get_driver
from module_05.sauce_func_lib.inventory import get_inventory
from module_05.sauce_func_lib.login import login


def test_valid_user():
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 5)
    driver.get('https://www.saucedemo.com/')
    login(wait, 'standard_user', 'secret_sauce')
    items = get_inventory(wait)
    assert len(items) > 0, 'Inventory should be loaded'
    assert items[0].title == 'Sauce Labs Backpack'
    assert items[1].title == 'Sauce Labs Bike Light'
    assert items[2].title == 'Sauce Labs Bolt T-Shirt'
    assert items[3].title == 'Sauce Labs Fleece Jacket'
    assert items[4].title == 'Sauce Labs Onesie'
    assert items[5].title == 'Test.allTheThings() T-Shirt(Red)'




"""def test_invalid_user():
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 5)
    driver.get('https://www.saucedemo.com/')
    login(wait, 'blahblahblah', 'blahblehbleh')"""

