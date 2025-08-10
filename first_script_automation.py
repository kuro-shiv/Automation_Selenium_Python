from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.google.com")
search = driver.find_element(By.NAME, "q")
search.send_keys("Selenium with Python")
search.submit()

time.sleep(3)
driver.quit()