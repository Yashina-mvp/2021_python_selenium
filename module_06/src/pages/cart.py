"""Cart Page"""
from selenium.webdriver.remote.webdriver import WebDriver
from module_06.src.elements.base_page_element import BasePageElement
from module_06.src.elements.header import Header
from module_06.src.locators.checkoutfirst import CartLocator
from module_06.src.pages.base_page import BasePage
from module_06.src.pages.inventory_details import InventoryDetailsPage

_URL = 'https://www.saucedemo.com/cart.html'


class CheckoutPage(BasePage):

    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, _URL, timeout)
        self.header = Header(self._wait)
        self._checkout_btn = BasePageElement(CartLocator.CHECKOUT, wait=self._wait, root=root)

    def click_checkout(self):
        self._checkout_btn.click()
        return InventoryDetailsPage(self._wait._driver, self._wait._timeout)