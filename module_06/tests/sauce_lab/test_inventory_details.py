"""Test cases for inventory item"""
from module_06.src.elements.inventory_item import InventoryItem
from module_06.src.pages.login import LoginPage
from module_06.tests.common.test_base import TestBase

_DEF_USER = 'standard_user'

_DEF_PASSWORD = 'secret_sauce'


class TestInventoryDetails(TestBase):

    def test_inventory_details(self):
        """test inventory prices"""
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[0]
        first_item: InventoryItem
        details_page = first_item.open_details()
        print('#' * 80)
        print(f'\n\nTitle {details_page.get_title()}')
        print(f'Description{details_page.get_description()}')
        print(f'Price: {details_page.get_price()}')
        details_page.add_to_cart()
        print(f'Total elements in cart: {details_page.header.get_total_cart_items()}')
        details_page.remove_from_cart()
        details_page.back()
        inventory_page.products.reload()
        assert len(inventory_page.products) == 6, 'Inventory len should be 6'

    # TEST SAUCE-LAB-4
    def test_item1(self):
        page = LoginPage(self.driver)
        page.open()
        inventory_page = page.login(_DEF_USER, _DEF_PASSWORD)
        first1 = inventory_page.products[0]
        first1: InventoryItem
        details_page = first1.open_details()
        print('#' * 80)
        print(f'\n\nTitle {details_page.get_title()}')
        print(f'Description{details_page.get_description()}')
        print(f'Price: {details_page.get_price()}')

    # TEST SAUCE-LAB-5
    def test_item2(self):
        page = LoginPage(self.driver)
        page.open()
        inventory_page = page.login(_DEF_USER, _DEF_PASSWORD)
        second2 = inventory_page.products[1]
        second2: InventoryItem
        details_page = second2.open_details()
        print('#' * 80)
        print(f'\n\nTitle {details_page.get_title()}')
        print(f'Description{details_page.get_description()}')
        print(f'Price: {details_page.get_price()}')

    # TEST SAUCE-LAB-6
    def test_item3(self):
        page = LoginPage(self.driver)
        page.open()
        inventory_page = page.login(_DEF_USER, _DEF_PASSWORD)
        third3 = inventory_page.products[2]
        third3: InventoryItem
        details_page = third3.open_details()
        print('#' * 80)
        print(f'\n\nTitle {details_page.get_title()}')
        print(f'Description{details_page.get_description()}')
        print(f'Price: {details_page.get_price()}')

    # TEST SAUCE-LAB-7
    def test_item4(self):
        page = LoginPage(self.driver)
        page.open()
        inventory_page = page.login(_DEF_USER, _DEF_PASSWORD)
        fourth4 = inventory_page.products[3]
        fourth4: InventoryItem
        details_page = fourth4.open_details()
        print('#' * 80)
        print(f'\n\nTitle {details_page.get_title()}')
        print(f'Description{details_page.get_description()}')
        print(f'Price: {details_page.get_price()}')

    # TEST SAUCE-LAB-8
    def test_item5(self):
        page = LoginPage(self.driver)
        page.open()
        inventory_page = page.login(_DEF_USER, _DEF_PASSWORD)
        fifth5 = inventory_page.products[4]
        fifth5: InventoryItem
        details_page = fifth5.open_details()
        print('#' * 80)
        print(f'\n\nTitle {details_page.get_title()}')
        print(f'Description{details_page.get_description()}')
        print(f'Price: {details_page.get_price()}')

    # TEST SAUCE-LAB-9
    def test_item6(self):
        page = LoginPage(self.driver)
        page.open()
        inventory_page = page.login(_DEF_USER, _DEF_PASSWORD)
        sixth6 = inventory_page.products[5]
        sixth6: InventoryItem
        details_page = sixth6.open_details()
        print('#' * 80)
        print(f'\n\nTitle {details_page.get_title()}')
        print(f'Description{details_page.get_description()}')
        print(f'Price: {details_page.get_price()}')
