"""Sauce Login Tests"""

import pytest

from module_06.src.pages.login import LoginPage
from module_06.tests.common.test_base import TestBase

LOGIN_DATA = [
    ('standard_user', 'secret_sauce'),
    ('performance_glitch_user', 'secret_sauce'),
    ('problem_user', 'secret_sauce'),
]

_DEF_USER = 'standard_user'
_DEF_PASSWORD = 'secret_sauce'

ERROR_MSG = 'Epic sadface: Username and password do not match any user in this service'


class TestLogin(TestBase):

    @pytest.mark.sanity
    @pytest.mark.login
    @pytest.mark.parametrize('user, password', LOGIN_DATA)
    # TEST SAUCE-LAB-1
    def test_valid_user(self, user: str, password: str):
        page = LoginPage(self.driver)
        page.open()
        page.login(user, password)

    @pytest.mark.regression
    @pytest.mark.login
    # TEST SAUCE-LAB-2
    def test_invalid_user(self):
        page = LoginPage(self.driver)
        page.open()
        page.login('standard_user', 'invalid_password')
        error_msg = page.get_error_message()
        assert error_msg is not None, 'Error message should be displayed for Invalid login'
        assert error_msg == ERROR_MSG, f'Error message should be {ERROR_MSG}'

    # TEST SAUCE-LAB-3
    def test_burger_logout(self):
        page = LoginPage(self.driver)
        page.open()
        login_inventory = page.login(_DEF_USER, _DEF_PASSWORD)
        login_inventory.header.open_menu()
        login_inventory.header.logout()
