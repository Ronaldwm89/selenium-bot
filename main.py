from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.python.org'
#url = 'https://www.amazon.com.br/PlayStation®5-Digital-Pacote-ASTRO-Turismo/dp/B0F7Z9F9SD/ref=sr_1_3?crid=2HOJPMTUYXJL6&dib=eyJ2IjoiMSJ9.Wnl7-AoF2oNXVfTvaJKW6xi5CAzwVuXZb6o9qoNE71Sg036Xl4tDqfUmf8C4zRZFywejAUxfz8ij93BCzepig3Mg9Gngx2XHph4U9Lf3QBf0aYDRSmrsrr8i6cZBDPS3qeWWIe-npmLV377kVHGJ-hFRt2hlHv6Ir4-amUM0_UlOX5M7-mmSY7-tkhUqd_u1Jauj1LW3Td55Pc99uxw1fK13pJLSLjBPjKQfcgZluFAP2klMpMq4FOPn6kxaN3U2GwZ-josiKb3BjObfS82RbbhlsDoqtqJSgeyl2J8oEuM.V2hOZy3NqJBvXPyImu2RxRFmVGCIQ2TxtgsA2GeqWdo&dib_tag=se&keywords=playstation+5&qid=1754091075&sprefix=playstat%2Caps%2C226&sr=8-3&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147'

crhome_options = webdriver.ChromeOptions()
crhome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=crhome_options)
driver.get(url)


upcoming_events = driver.find_elements(By.CLASS_NAME, 'event-widget')
for event in upcoming_events: 
    fecha = event.find_elements(By.TAG_NAME, 'time')
    events = event.find_elements(By.CSS_SELECTOR, 'li a')

    diccionario = {i: {'time': fecha.text, 'name': events.text} for i, (fecha, events) in enumerate(zip(fecha, events))}
    print(diccionario)#



#precio = driver.find_element(By.CLASS_NAME, "a-price-whole")
#centimos = driver.find_element(By.CLASS_NAME, "a-price-fraction")#
#print(f'{precio.text},{centimos.text}')#


#driver.close()#cierra la pestaña del navegador
#driver.quit() #cierra el navegador completo
