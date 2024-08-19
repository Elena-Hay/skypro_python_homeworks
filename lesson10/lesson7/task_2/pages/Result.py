from selenium.webdriver.common.by import By
import allure


class Result:

    def __init__(self, driver):
       self.driver = driver

    @allure.step("Посмотреть результат")
    def res(self) -> str:
        """
        Эта функция возвращает текст с результатом вычисления калькулятора
        """
        return self.driver.find_element(By.CSS_SELECTOR, '.screen').text
