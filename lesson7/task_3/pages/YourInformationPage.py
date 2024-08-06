from selenium.webdriver.common.by import By


class Informations:

    def __init__(self, driver):
        self.driver = driver

    def first_name(self, f_name):
        self.driver.find_element(By.ID, 'first-name').send_keys(f_name)

    def last_name(self, l_name):
        self.driver.find_element(By.ID, 'last-name').send_keys(l_name)

    def postal_code(self, post_code):
        self.driver.find_element(By.ID, 'postal-code').send_keys(post_code)

    def button_continue(self):
        self.driver.find_element(By.ID, 'continue').click()
