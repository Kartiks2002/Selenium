from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)
driver.get("https:/rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.XPATH, '//a[@class="blinkingText"]').click()

windows_opened = driver.window_handles
driver.switch_to.window(windows_opened[1])

mail_id = driver.find_element(By.XPATH, '//a[@href="mailto:mentor@rahulshettyacademy.com"]').text

driver.switch_to.window(windows_opened[0])
driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(mail_id)
driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('learning')

# driver.find_element(By.XPATH, '//input[@value="admin"]').click()
# driver.find_element(By.XPATH, '//button[@id="okayBtn"]').click()

# driver.find_element(By.XPATH, '//select[@xpath="1"]').click()
# driver.find_element(By.XPATH, '//option[@value="stud"]').click()

driver.find_element(By.XPATH, '//input[@id="terms"]').click()
driver.find_element(By.XPATH, '//input[@id="signInBtn"]').click()
