"""Browsing Example with Selenium"""

from pathlib import Path
from selenium import webdriver

def get_project_root() -> Path:
    """Get project root path"""
    return Path(__file__).parent.parent

def get_chrome_path() -> Path:
    """Get chrome driver path"""
    root = get_project_root()
    return root.joinpath('drivers', 'chromedriver')


def print_page_details(driver: webdriver.Remote) -> None:
    """get page details"""
    print(f'Current title: {driver.title}')
    print(f'Current url: {driver.current_url}')
   #print(f'Current source: {driver.page_source}')

driver = webdriver.Chrome(executable_path=get_chrome_path())

driver.get('https://www.google.com/')
print_page_details(driver)

driver.get('https://www.mlb.com/es')
print_page_details(driver)


driver.get('https://www.nytimes.com/es/')
driver.refresh()
print_page_details(driver)

driver.back()
driver.back()
print_page_details(driver)

print(driver.get_cookies())
print(driver.application_cache)

print(driver.find_elements_by_partial_link_text("SOCzOAOac8uhByk5ZGU2Zg=="))

driver.quit()

