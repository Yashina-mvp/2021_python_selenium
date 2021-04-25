from common.webdriver_factory import get_driver

driver = get_driver('chrome')
driver.implicitly_wait(10)
driver.get('https://www.google.com')

first_body_son = driver.find_elements_by_xpath("//body/div")