import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service  # Service for driver path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Optional: specify the path to your ChromeDriver
# service_obj = Service('path_to_chromedriver.exe')
# driver = webdriver.Chrome(service=service_obj)

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open Wikipedia
driver.get("https://www.wikipedia.com")

# ----------- INFORMATION ABOUT THE PAGE -----------
print("Page Title:", driver.title)        # Gets the title of the page
print("Current URL:", driver.current_url) # Gets the current page URL

# ----------- LOCATORS -----------

# 1. Using ID
search_box = driver.find_element(By.ID, 'searchInput')
search_box.send_keys("Selenium")

# 2. Using Class Name
search_button = driver.find_element(By.CLASS_NAME, 'pure-button')
search_button.click()

# Wait until next page loads and content is available
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'firstHeading'))
)

# 3. Using Tag name and ID (XPath)
heading = driver.find_element(By.XPATH, "//h1[@id='firstHeading']")
print("Article Heading (via XPath):", heading.text)

# 4. Using CSS Selector
content = driver.find_element(By.CSS_SELECTOR, "div.mw-parser-output > p")
print("First paragraph (via CSS Selector):", content.text)

# 5. Using Link Text - Navigating using visible link
# Scroll to the bottom to find a link
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Wikimedia Foundation").click()

# Wait for the page to load
WebDriverWait(driver, 10).until(
    EC.title_contains("Wikimedia")
)

print("New Page Title:", driver.title)
print("New URL:", driver.current_url)

# Optional: Navigate back
driver.back()
print("Went back to:", driver.title)

# Wait a bit and close
time.sleep(5)
driver.quit()
