from module_06.src.elements.inventory_item import InventoryItem
from module_06.src.pages.cart import CheckoutPage
from module_06.src.pages.login import LoginPage
from module_06.tests.common.test_base import TestBase

_DEF_USER = 'standard_user'

_DEF_PASSWORD = 'secret_sauce'


class TestYourCart(TestBase):

    # TEST SAUCE-LAB-13
    def test_checkout_click(self):
        """test item added to cart"""
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        item_picked = inventory_page.products[0]
        item_picked: InventoryItem
        item_picked.click_add()
        inventory_page.header.goto_cart()
        CheckoutPage.click_checkout()
