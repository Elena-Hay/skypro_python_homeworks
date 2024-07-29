from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for n in range(5):
    driver.find_element(By.CSS_SELECTOR, 'div.example button').click()
    sleep(1)

delete_button = driver.find_elements(By.CSS_SELECTOR, '.added-manually')
print("Размер списка Chrome:", len(delete_button))
driver.quit()
