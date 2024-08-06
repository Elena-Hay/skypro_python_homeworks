from selenium.webdriver.common.by import By


class Overview:

    def __init__(self, driver):
        self.driver = driver

    def result(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
