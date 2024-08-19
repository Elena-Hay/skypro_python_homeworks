from selenium.webdriver.common.by import By
import allure


class AuthPage:
    url = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть сайт")
    def open(self) -> None:
        """
        Эта функция открывает сайт
        """
        self.driver.get(self.url)

    @allure.step("Авторизоваться")
    def authorization(self, login: str, password: str) -> None:
        """
        Эта функция принимает на вход логин и пароль. Находит поля по локаторам и вводит значения
        """
        self.driver.find_element(By.ID, 'user-name').send_keys(login)
        self.driver.find_element(By.ID, 'password').send_keys(password)

    @allure.step("Нажать кнопку Login")
    def button(self) -> None:
        """
        Эта функция находит на странице по локатору кнопку Login и кликает на нее
        """
        self.driver.find_element(By.ID, 'login-button').click()
