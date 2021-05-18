"""Common functions"""
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def write_to_input(wait: WebDriverWait, locator: By, value: str):
    """Clear and write to input field
    :param wait: Instance of webdriver wait.
    :param locator: ---
    :param value: Value to write
    :return:
    """
    element = wait.until(EC.element_to_be_clickable(locator))
    element.clear()
    element.send_keys(value)


def click(wait: WebDriverWait, locator: By):
    element = wait.until(EC.element_to_be_clickable(locator))
    element.click()


def get_text(wait: WebDriverWait, locator: By) -> None:
    """Get text"""
    # Try - Catch delay mas grande
    try:
        element = wait.until(EC.visibility_of_element_located(locator))
        return element.text
    except TimeoutException:
        return None
