
from common.webdriver_factory import get_driver

driver = get_driver('chrome')
driver.get('https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&dsh=S1644451455%3A1618463507271541&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp')

name = driver.find_element_by_id('firstName')
name.send_keys('Yashi')
last_name = driver.find_element_by_id('lastName')
last_name.send_keys('Jacuinde')
user_name = driver.find_element_by_id('username')
user_name.send_keys('yashikochan90')
password = driver.find_element_by_name('Passwd')
password.send_keys('Hibiscus121290')
password = driver.find_element_by_name('ConfirmPasswd')
password.send_keys('Hibiscus121290')
next = driver.find_element_by_class_name('VfPpkd-RLmnJb')
next.click()
driver.quit()