
from common.webdriver_factory import get_driver

driver = get_driver('chrome')
driver.get('https://formsmarts.com/html-form-example')
driver.switch_to_frame(driver.find_element_by_class_name('fs_embed'))

first_name = driver.find_element_by_id('u_ROn_4607')
first_name.clear()
first_name.send_keys('Yashi')
last_name = driver.find_element_by_id('u_ROn_338354')
last_name.clear()
last_name.send_keys('Jacuinde')
email = driver.find_element_by_id('u_ROn_4608')
email.clear()
email.send_keys('cukiboo@gmail.com')
inquiry = driver.find_element_by_id('u_ROn_4609')
inquiry.clear()
inquiry.send_keys(('automation practice'))

#driver.quit()