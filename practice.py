import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# radio button
radio_options = driver.find_elements(By.CSS_SELECTOR, 'input[type="radio"]')
print(len(radio_options))
for option in radio_options:
    if option.get_attribute("value") == 'radio2':
        option.click()
        assert option.is_selected()
# driver.find_element(By.XPATH, '//input[@id="autocomplete"]').send_keys('Spain')
#
# # Dropdown
# driver.find_element(By.XPATH, '//select[@id="dropdown-class-example"]').click()
# driver.find_element(By.XPATH, '//option[@value="option1"]').click()
#
# driver.find_element(By.XPATH, '//input[@id="checkBoxOption1"]').click()
# driver.find_element(By.CSS_SELECTOR, 'input[id="checkBoxOption2"]').click()
# driver.find_element(By.CSS_SELECTOR, 'input[id="checkBoxOption3"]').click()

time.sleep(10)