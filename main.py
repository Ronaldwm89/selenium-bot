#Project play click cookies with a bot using Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

crhome_options = webdriver.ChromeOptions()
crhome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options = crhome_options)
driver.get('https://ozh.github.io/cookieclicker')

time.sleep(5)  # Wait for the page to load
language = driver.find_element(By.XPATH, '//*[@id="langSelect-ES"]')
language.click()

time.sleep(5)

inicio = time.time()# Wait for the language to change
while time.time() - inicio < 20:
    cookie = driver.find_element(By.CSS_SELECTOR, '#bigCookie')
    cookie.click()
   

