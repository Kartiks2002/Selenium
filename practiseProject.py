import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://rahulshettyacademy.com/angularpractice')

driver.find_element(By.XPATH, '//a[contains(@href,"/angularpractice/shop")]').click()
appcard_list = driver.find_elements(By.XPATH, '//app-card')
# print(len(appcard_list))

# print(driver.find_element(By.XPATH, '//h4[@class="card-title"]').text)
for appcard in appcard_list:
    product = appcard.find_element(By.XPATH, '//h4[@class="card-title"]/a').text
    if product == "Blackberry":
        appcard.find_element(By.XPATH, '//button[@xpath="1"]').click()

driver.find_element(By.XPATH, '//a[@class="nav-link btn btn-primary"]').click()
driver.find_element(By.XPATH, '//button[@class="btn btn-success"]').click()
driver.find_element(By.XPATH, '//input[@id="country"]').send_keys('In')
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.XPATH, '//a[text()="India"]').click()
driver.find_element(By.XPATH, '//div[@class="checkbox checkbox-primary"]').click()
driver.find_element(By.XPATH, '//input[@type="submit"]').click()
# success_text_req = 'Success! Thank you! Your order will be delivered in next few weeks :-).'
succes_text_got = driver.find_element(By.XPATH, '//div[@class="alert alert-success alert-dismissible"]').text

assert "Success" in succes_text_got
