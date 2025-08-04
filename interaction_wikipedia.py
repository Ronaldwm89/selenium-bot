from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

crhome_options = webdriver.ChromeOptions()
crhome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=crhome_options)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[2]/a[1]')
#print(count.text)

icone = driver.find_element(By.LINK_TEXT, 'Search')
icone.click()

search_bar = driver.find_element(By.NAME, 'search')
search_bar.send_keys('Python', Keys.ENTER)
search_bar.send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN)

#count.click()#