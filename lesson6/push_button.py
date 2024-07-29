from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()

waiter = WebDriverWait(driver, 200)
waiter.until(
    EC.text_to_be_present_in_element( (By.CSS_SELECTOR, ".bg-success"), "Data loaded with AJAX get request.")
)

txt = driver.find_element(By.CSS_SELECTOR, 'p.bg-success').text
print("Текст из зеленой плашки:", txt)

driver.quit()
