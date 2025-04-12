import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.maximize_window()

driver.get('https://the-internet.herokuapp.com/windows')
driver.find_element(By.XPATH, '//a[@href="/windows/new"]').click()

windows_opened = driver.window_handles
driver.switch_to.window(windows_opened[1])
print(driver.find_element(By.TAG_NAME, 'h3').text)

driver.switch_to.window(windows_opened[0])
print(driver.find_element(By.TAG_NAME, 'h3').text)