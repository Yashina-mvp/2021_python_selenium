"""tik tok"""
from typing import Tuple

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from common.webdriver_factory import get_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.by import By


def search(wait: WebDriverWait, value: str):
    locator = (By.NAME, 'q')
    textbox = wait.until(EC.element_to_be_clickable(locator))
    textbox.clear()
    textbox.send_keys(value)

    search_button = (By.XPATH, "//button[@type= 'submit']")
    button = wait.until(EC.element_to_be_clickable(search_button))
    button.click()


def print_results(wait: WebDriverWait):
    "Print search results information"
    list_results = (By.XPATH, "//a[contains(@class, 'result-item')]")
    results = wait.until(EC.visibility_of_all_elements_located(list_results))
    print(f'results:{len(results)}')
    for result in results:
        print(result.text)
        title = result.find_element_by_xpath(".//*[contains(@class, ' title ')]")
        sub_title = result.find_element_by_xpath(".//*[contains(@class, 'sub-title')]")
        description = result.find_element_by_xpath(".//*[contains(@class, 'desc]')]")
        print(f' {title.text:20}  | {sub_title.text:20} | {description.text:20}')


if __name__ == '__main__':
    my_driver = get_driver('chrome')
    my_wait = WebDriverWait(my_driver, 3)

    # go to tik tok
    my_driver.get('https://www.tiktok.com/?lang=es')

    # Search
    search(my_wait, 'Python')

    # Show Results info
    print_results(my_wait)

    # Quit
    my_driver.quit()
