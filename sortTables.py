import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Open Chrome Browser
driver = webdriver.Chrome()
driver.implicitly_wait(10)
# Maximax the window
driver.maximize_window()
# Go to the URL
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/offers')
driver.find_element(By.CSS_SELECTOR, 'th:nth-child(1)').click()
vegetables = driver.find_elements(By.XPATH, '//tr/td[1]')
vlist = []
for v in vegetables:
    name = vlist.append(v.text)
assert vlist == sorted(vlist)
print(vlist)