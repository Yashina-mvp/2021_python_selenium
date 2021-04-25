from common.webdriver_factory import get_driver
from selenium.webdriver.support.ui import Select

driver = get_driver('chrome')
driver.implicitly_wait(5)
driver.get('https://formsmarts.com/form/axi?mode=h5')

driver.find_element_by_name('u_BS9_60857').send_keys('Yashi')
driver.find_element_by_name('u_BS9_60858').send_keys('G Jacuinde')
driver.find_element_by_name('u_BS9_60859').send_keys('cukiboo@gmail.com')
driver.find_element_by_name('u_BS9_60860').send_keys('Luigi pirandello 5630')
element = driver.find_element_by_name('u_BS9_60871')
dropdown = Select(element)
print(f'Is multiple selection enabled: {dropdown.is_multiple}')
dropdown.select_by_visible_text('Mexico')
print(f'Current selection: {dropdown.first_selected_option.text}')
check_in_date = driver.find_element_by_name('u_BS9_60861')
check_in_date.clear()
check_in_date.send_keys('15/04/2021')
number_of_nights = driver.find_element_by_name('u_BS9_60870')
number_of_nights.clear()
number_of_nights.send_keys('4')
continue_btn = driver.find_element_by_name('submit')
continue_btn.click()
