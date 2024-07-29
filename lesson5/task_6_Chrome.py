from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/login") 

username = driver.find_element(By.CSS_SELECTOR, '#username')
username.send_keys("tomsmith")

password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys("SuperSecretPassword!")

sleep(1)

login_button = driver.find_element(By.CSS_SELECTOR, 'button').click()

sleep(3)

driver.quit()
