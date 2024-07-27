from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(5)   

element_close = driver.find_element(By.CSS_SELECTOR, '.modal-footer p')
element_close.click()
sleep(3)

driver.quit()
