from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


crhome_options = webdriver.ChromeOptions()
crhome_options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=crhome_options)
driver.get('https://secure-retreat-92358.herokuapp.com')

fname = driver.find_element(By.NAME, 'fName')
fname.send_keys('Ronald', Keys.TAB)

lname = driver.find_element(By.NAME, 'lName')
lname.send_keys('Medina', Keys.TAB)

email = driver.find_element(By.NAME, 'email')
email.send_keys('ryls.log@yahoo.com', Keys.ENTER)#