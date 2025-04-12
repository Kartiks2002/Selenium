import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Open Chrome Browser
driver = webdriver.Chrome()
driver.implicitly_wait(10)
# Maximax the window
driver.maximize_window()
# Go to the URL
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
# Search for something in the searchbox
driver.find_element(By.XPATH, '//input[@class="search-keyword"]').send_keys('ber')
driver.find_element(By.XPATH, '//button[@class="search-button"]').click()
# Get the list of items
items = driver.find_elements(By.XPATH,'//div[@class="products"]/div[@class="product"]')
# print(items)
# print(len(items))
for item in items:
    item.find_element(By.XPATH, 'div/button').click()

# Add to cart
driver.find_element(By.XPATH, '//a[@class="cart-icon"]').click()
driver.find_element(By.XPATH, '//div[@class="cart-preview active"]/div[@class="action-block"]/button').click()
# time.sleep(2) # used the implicitly_wait instead
#
# Calculate sum
item_totals = driver.find_elements(By.XPATH, '//td[5]/p')
# print(len(item_totals))
sum = 0
for i in item_totals:
    # print(i.text)
    sum += int(i.text)
# print(sum)

# Validate the calculated sum
totAmt = int(driver.find_element(By.XPATH, '//span[@class="totAmt"]').text)
assert sum == totAmt

# Apply the Promo code
driver.find_element(By.XPATH, '//input[@class="promoCode"]').send_keys('rahulshettyacademy')
driver.find_element(By.XPATH, '//button[@class="promoBtn"]').click()

# # Get the discount percent and recalculate
discount_percent = float(driver.find_element(By.XPATH, '//span[@class="discountPerc"]').text[:-1])
totalAfterDiscount = float(driver.find_element(By.XPATH, '//span[@class="discountAmt"]').text)

calculatedTotal = sum - ((sum*discount_percent)/100)
assert calculatedTotal == totalAfterDiscount

# Place order
driver.find_element(By.XPATH, '//button[@xpath="1"]').click()

# Choose Country, Agree to the T&C, Proceed
# driver.find_element(By.XPATH, '//select[@xpath="1"]').click()
# driver.find_element(By.XPATH, '//option[@value="Italy"]').click()
#
# driver.find_element(By.XPATH, '//input[@type="checkbox"]').click()
#
# driver.find_element(By.XPATH, 'button[@xpath="1"]').click()



print("hello world")


















time.sleep(5)