from selenium import webdriver
from selenium.webdriver.common.by import By

crhome_options = webdriver.ChromeOptions()
crhome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=crhome_options)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[2]/a[1]')
print(count.text)#