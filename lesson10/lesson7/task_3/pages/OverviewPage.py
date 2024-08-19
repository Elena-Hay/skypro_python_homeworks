from selenium.webdriver.common.by import By
import allure


class Overview:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Получить итоговую сумму покупок")
    def result(self) -> str:
        """
        Эта функция по локатору находит общую сумму заказа и возвращает текст
        """
        return self.driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
