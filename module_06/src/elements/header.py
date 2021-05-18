""""Abstraction to interact with inventory items."""
from selenium.webdriver.support.wait import WebDriverWait
from module_06.src.elements.base_page_element import BasePageElement
from module_06.src.locators.header import HeaderLoc


class Header:
    """Represents inventory item"""

    def __init__(self, wait: WebDriverWait):
        self._wait = wait
        self._shopping_cart = BasePageElement(HeaderLoc.SHOPPING_CART, wait=wait)
        self._badge = BasePageElement(HeaderLoc.BADGE, wait=wait)
        self._burger_btn = BasePageElement(HeaderLoc.BURGER_BTN, wait=wait)
        self._logout_option = BasePageElement(HeaderLoc.LOGOUT_OPT, wait=wait)

    def get_total_cart_items(self) -> int:
        """Get total items in the cart"""
        try:
            return int(self._badge.get_text())
        except Exception:
            return 0

    def goto_cart(self):
        """Go to cart"""
        self._shopping_cart.click()
        return (self._wait._driver, self._wait._timeout)

    def open_menu(self):
        """Open menu"""
        self._burger_btn.click()

    def logout(self):
        """logout page"""
        self._logout_option.click()
