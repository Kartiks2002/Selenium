import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# Hover
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, '//button[@id="mousehover"]')).perform()
action.click(driver.find_element(By.XPATH, '//a[@href="#top"]')).perform()
time.sleep(5)