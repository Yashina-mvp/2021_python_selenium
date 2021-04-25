from common.webdriver_factory import get_driver

driver = get_driver('chrome')
driver.implicitly_wait(10)
driver.get('https://www.amazon.com.mx')

#one element = driver.find_element_by_xpath("")

print('A elements:')
a_elements = driver.find_elements_by_xpath("//a") #List: [WebElement, WebElement, WebElement]
for element in a_elements:
    print(element.text)

print('Head children: ')
head_children = driver.find_elements_by_xpath("//head/*")
for element in head_children:
    print(element.text)

driver.quit()