import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service

# service_obj = Service('C:/Users/H606223/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')
# driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.wikipedia.com")
# print(driver.title)
# print(driver.current_url)

# ID, Xpath, CSSSelector , Classname, Name, LinkText
driver.find_element(By.ID, 'searchInput').send_keys("Selenium")
driver.find_element(By.CLASS_NAME, 'pure-button').click()

# Xpath //tagname[@attribute='value']
# CSS   tagname[attribute='value']









time.sleep(5)