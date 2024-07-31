from selenium import webdriver
from selenium.webdriver.common.by import By


def test_buy():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, 'user-name').send_keys("standard_user")
    driver.find_element(By.ID, 'password').send_keys("secret_sauce")
    driver.find_element(By.ID, 'login-button').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
    driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()
    driver.find_element(By.ID, 'checkout').click()
    driver.find_element(By.ID, 'first-name').send_keys("Елена")
    driver.find_element(By.ID, 'last-name').send_keys("Хайбулкина")
    driver.find_element(By.ID, 'postal-code').send_keys("432029")
    driver.find_element(By.ID, 'continue').click()
    res = driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
    assert res == "Total: $58.29"
    driver.quit()
