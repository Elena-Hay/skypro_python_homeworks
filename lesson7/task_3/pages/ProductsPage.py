from selenium.webdriver.common.by import By


class Products:

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

    def cart(self):
        self.driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()
