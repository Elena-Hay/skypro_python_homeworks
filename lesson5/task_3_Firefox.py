from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()

for n in range(3):
    driver.get("http://uitestingplayground.com/classattr")
    click_button = driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()
    sleep(1)

    wait = WebDriverWait(driver, timeout=2)
    alert = wait.until(lambda d : d.switch_to.alert)
    text = alert.text
    alert.accept()
    
driver.quit()