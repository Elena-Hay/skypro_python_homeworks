from selenium.webdriver.common.by import By
import allure


class Cart:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Кликнуть на кнопку Checkout")
    def check(self) -> None:
        """
        Эта функция по локатору находит кнопку Checkout и нажимает на нее
        """
        self.driver.find_element(By.ID, 'checkout').click()
