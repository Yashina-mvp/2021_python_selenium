from selenium.webdriver.common.keys import Keys
from common.webdriver_factory import get_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def login(wait: WebDriverWait, email:str, secret:str):
    "Login to pinterest"
    #Open log in Dialog
    login_btn_locator = (By.XPATH, "//*[@id='__PWS_ROOT__']/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/button")

    login_btn = wait.until(EC.element_to_be_clickable(login_btn_locator))
    login_btn.click()

    #set users
    user_locator = (By.ID, 'email')
    user = wait.until(EC.element_to_be_clickable(user_locator))
    user.clear()
    user.send_keys(email)

    #set password
    password_locator = (By.ID, 'password')
    password = wait.until(EC.element_to_be_clickable(password_locator))
    password.clear()
    password.send_keys(secret)

    #Submit
    submit_btn_locator = (By.XPATH, "//*[@data-test-id= 'registerFormSubmitButton']/button")
    submit_btn = wait.until(EC.element_to_be_clickable(submit_btn_locator))
    submit_btn.click()

def search(wait: WebDriverWait, value: str):
    "Search in pinterest"
    textbox_locator = (By.XPATH, "//*[@data-test-id= 'search-box-input']")
    textbox = wait.until(EC.element_to_be_clickable(textbox_locator))
    textbox.clear()
    textbox.send_keys(value)
    textbox.send_keys(Keys.ENTER)


if __name__ =='__main__':
    my_driver = get_driver('chrome')
    my_wait = WebDriverWait(my_driver, 3)

    #Go to pinterest
    my_driver.get('https://www.pinterest.com.mx')

    #login
    login(my_wait, 'qamindstester@gmail.com', 'Q@Minds4%')

    #Search Selenium
    search(my_wait, 'Selenium')

    #Exit
    my_driver.quit()
