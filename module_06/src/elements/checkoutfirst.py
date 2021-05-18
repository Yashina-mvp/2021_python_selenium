from selenium.webdriver.support.wait import WebDriverWait

from module_06.src.elements.base_page_element import BasePageElement
from module_06.src.locators import checkoutfirst


class CheckoutFirst:

    def __init__(self, wait: WebDriverWait):
        self._wait = wait
        self._checkout_btn = BasePageElement(checkoutfirst.CHECKOUT, wait=wait)

