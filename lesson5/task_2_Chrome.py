from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

for n in range(3):
    driver.get("http://uitestingplayground.com/dynamicid")
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
    sleep(1)

driver.quit()
