from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalcPage:
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть сайт")
    def open(self) -> None:
        """
        Эта функция открывает сайт
        """
        self.driver.get(self.url)

    @allure.step("Изменить время ожидания калькулятора")
    def delay(self, time: int) -> None:
        """
        # Эта функция стирает значение в поле по локатору #delay, принимает на вход значение time
        """
        self.driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self.driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(time)
    
    @allure.step("Набрать на калькуляторе сумму цифр 7 и 8, нажать знак '='")
    def sum(self) -> None:
        """
        Эта функция набирает на калькуляторе: 7+8=
        """
        self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="="]').click()

    @allure.step("Подождать вычисление")
    def wait(self, time: int) -> None:
        """
        Эта функция принимает на вход время, в течение которого ожидает появления в окне по селектору 
        ".screen" значения "15"
        """
        waiter = WebDriverWait(self.driver, time)
        waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )
