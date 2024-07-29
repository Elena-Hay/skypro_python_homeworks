from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")

driver.find_element(By.CSS_SELECTOR, '#newButtonName').send_keys("skypro")

driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()

txt = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text
print("Текст новой кнопки:", txt)

driver.quit()
