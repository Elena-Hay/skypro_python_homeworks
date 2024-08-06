from selenium.webdriver.common.by import By


class AuthPage:
    url = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def authorization(self, login, password):
        self.driver.find_element(By.ID, 'user-name').send_keys(login)
        self.driver.find_element(By.ID, 'password').send_keys(password)

    def button(self):
        self.driver.find_element(By.ID, 'login-button').click()
