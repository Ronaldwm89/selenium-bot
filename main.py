#Project play click cookies with a bot using Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

crhome_options = webdriver.ChromeOptions()
crhome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options = crhome_options)
driver.get('https://ozh.github.io/cookieclicker')

time.sleep(2)  # Wait for the page to load
language = driver.find_element(By.XPATH, '//*[@id="langSelect-ES"]')
language.click()

time.sleep(3) #wait for the cookie to appear
five_seconds = time.time()
inicio = time.time() #inicio del tiempo de ejecucion
while time.time() - inicio < 40:
    cookie = driver.find_element(By.CSS_SELECTOR, '#bigCookie')# Find the cookie element and click it
    cookie.click()
    
    
    if time.time() - five_seconds > 5:
        prices = driver.find_elements(By.CSS_SELECTOR, '.price')
        
        for price in prices:
            print(price.text)
        
        print('acaban de pasar 5 segundos')#
        five_seconds = time.time()
        
    
   

print(time.time())
