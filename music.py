import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.youtube.com')
driver.find_element(By.XPATH, '//input[@name="search_query"]').send_keys('study music')
driver.find_element(By.CLASS_NAME, "ytSearchboxComponentSearchButton").click()
driver.find_element(By.ID, 'thumbnail').click()
# driver.find_element(By.CSS_SELECTOR, 'span[class="yt-icon-shape"]').click()

















time.sleep(10)