from common.webdriver_factory import get_driver


driver = get_driver('chrome')
driver.implicitly_wait(10)
#Go to page
driver.get('https://www.mlb.com/es/standings')

    #select league/ MLB /Division
element = driver.find_element_by_css_selector("#standings_index > main > div.container > div > div > div > div.standings__header-container.show-springtraining > div.standings__sub-nav.subNav.regularSeasonSubNav > div.sub-nav-filters > div:nth-child(2) > div:nth-child(1) > div > select > option:nth-child(2)")
element.click()
element_02 = driver.find_element_by_css_selector("#standings_index > main > div.container > div > div > div > div.standings__header-container.show-springtraining > div.standings__sub-nav.subNav.regularSeasonSubNav > div.sub-nav-filters > div:nth-child(2) > div:nth-child(1) > div > select > option:nth-child(3)")
element_02.click()
element_03 = driver.find_element_by_css_selector("#standings_index > main > div.container > div > div > div > div.standings__header-container.show-springtraining > div.standings__sub-nav.subNav.regularSeasonSubNav > div.sub-nav-filters > div:nth-child(2) > div:nth-child(1) > div > select > option:nth-child(1)")
element_03.click()

    #select standard
standard = driver.find_element_by_css_selector("#standings_index > main > div.container > div > div > div > div.standings__header-container.show-springtraining > div.standings__sub-nav.subNav.regularSeasonSubNav > div.sub-nav-filters > div:nth-child(2) > div:nth-child(2) > div > div:nth-child(1) > button")
standard.click()

    #select advance
advancing = driver.find_element_by_css_selector("#standings_index > main > div.container > div > div > div > div.standings__header-container.show-springtraining > div.standings__sub-nav.subNav.regularSeasonSubNav > div.sub-nav-filters > div:nth-child(2) > div:nth-child(2) > div > div:nth-child(2) > button")
advancing.click()

driver.quit()

