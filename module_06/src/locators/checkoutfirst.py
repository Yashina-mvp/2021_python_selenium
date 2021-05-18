"""Locators for Your Cart page"""
from selenium.webdriver.common.by import By


class CartLocator:
    CHECKOUT = (By.XPATH, "//*[@class='cart_footer']/a[contains(@class,'btn_action')]")
