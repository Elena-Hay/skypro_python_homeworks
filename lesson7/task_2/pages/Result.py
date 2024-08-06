from selenium.webdriver.common.by import By


class Result:

    def __init__(self, driver):
       self.driver = driver

    def res(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.screen').text