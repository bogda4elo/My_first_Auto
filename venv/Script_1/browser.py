from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print = time.strftime("%d/%m/%Y")

driver = webdriver.Chrome()
driver.get('https://www.y8.com/')

screenshot = driver.save_screenshot('www.y8.com.png')

driver.quit()

# pass
