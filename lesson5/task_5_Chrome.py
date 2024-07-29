from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/inputs") 

input = driver.find_element(By.CSS_SELECTOR, 'input')
input.send_keys("1000")
sleep(1)
input.clear()
sleep(1)
input.send_keys("999")
sleep(1)

driver.quit()
