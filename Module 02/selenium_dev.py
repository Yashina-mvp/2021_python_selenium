
    """Navigate Selenium Page"""

from common.webdriver_factory import get_driver

driver = get_driver('chrome')
driver.get('https://www.selenium.dev/')

for link in ['Downloads', 'Projects', 'Support', 'Blog']:
    element = driver.find_element_by_link_text(link)
    print('-' * 80)
    print( f'Hyperlink text: {element.text}')
    print(f'is it enabled? :{element.is_enabled()}')
    print(f'is it displayed? :{element.is_displayed()}')
    print(f'is it selected?: {element.is_selected()}')
    if element.is_enabled() and element.is_displayed():
        element.click()

driver.quit()