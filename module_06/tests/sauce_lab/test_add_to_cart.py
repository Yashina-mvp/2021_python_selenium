"""Test cases for add to cart"""
from module_06.src.elements.inventory_item import InventoryItem
from module_06.src.pages.login import LoginPage
from module_06.tests.common.test_base import TestBase

_DEF_USER = 'standard_user'

_DEF_PASSWORD = 'secret_sauce'


class TestAddCart(TestBase):

    # TEST SAUCE-LAB-10
    def _add_to_cart_item_main_page(self):
        """test item added to cart"""
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        item_picked = inventory_page.products[0]
        item_picked: InventoryItem
        item_picked.click_add()

    # TEST SAUCE-LAB-11
    def _add_to_cart_item_details(self):
        """test item added to cart"""
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        item_picked = inventory_page.products[2]
        item_picked: InventoryItem
        details_page = item_picked.open_details()
        details_page.add_to_cart()
        details_page.back()
        # assert 'remove-sauce-labs-bolt-t-shirt' == InventoryDetailsLoc.REMOVE_BTN

    # TEST SAUCE-LAB-12
    def test_remove_item1_main_page(self):
        """test item added to cart"""
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        item_picked = inventory_page.products[0]
        item_picked: InventoryItem
        item_picked.click_add()
        item_picked.remove_from_cart()


