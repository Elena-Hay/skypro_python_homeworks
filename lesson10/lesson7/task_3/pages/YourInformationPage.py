from selenium.webdriver.common.by import By
import allure


class Informations:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Заполнить поле First Name")
    def first_name(self, f_name: str) -> None:
        """
        Эта функция принимает на вход имя и вводит его в поле First Name
        """
        self.driver.find_element(By.ID, 'first-name').send_keys(f_name)

    @allure.step("Заполнить поле Last Name")
    def last_name(self, l_name: str) -> None:
        """
        Эта функция принимает на вход фамилию и вводит его в поле Last Name
        """
        self.driver.find_element(By.ID, 'last-name').send_keys(l_name)

    @allure.step("Заполнить поле Zip/Postal Code")
    def postal_code(self, post_code: str) -> None:
        """
        Эта функция принимает на вход почтовый индекс и вводит его в поле Zip/Postal Code
        """
        self.driver.find_element(By.ID, 'postal-code').send_keys(post_code)

    @allure.step("Нажать на кнопку Continue")
    def button_continue(self) -> None:
        """
        Эта функция по локатору находит кнопку Continue и кликает на нее
        """
        self.driver.find_element(By.ID, 'continue').click()
