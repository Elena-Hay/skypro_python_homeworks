from selenium.webdriver.common.by import By
import allure


class FilledForm:

    def __init__(self, driver):
       self.driver = driver

    @allure.step("Найти заполненное поле First name")
    def filled_first_name(self) -> str:
        """
        Эта функция находит элемент по локатору и возвращает значение атрибута в виде строки
        """
        return self.driver.find_element(By.ID, "first-name").get_attribute("class")

    @allure.step("Найти заполненное поле Last name")
    def filled_last_name(self) -> str:
        """
        Эта функция находит элемент по локатору и возвращает значение атрибута в виде строки
        """
        return self.driver.find_element(By.ID, "last-name").get_attribute("class")

    @allure.step("Найти заполненное поле Address")
    def filled_address(self) -> str:
        """
        Эта функция находит элемент по локатору и возвращает значение атрибута в виде строки
        """
        return self.driver.find_element(By.ID, "address").get_attribute("class")

    @allure.step("Найти заполненное поле Email")
    def filled_mail(self) -> str:
        """
        Эта функция находит элемент по локатору и возвращает значение атрибута в виде строки
        """
        return self.driver.find_element(By.ID, "e-mail").get_attribute("class")

    @allure.step("Найти заполненное поле Phone number")
    def filled_phone(self) -> str:
        """
        Эта функция находит элемент по локатору и возвращает значение атрибута в виде строки
        """
        return self.driver.find_element(By.ID, "phone").get_attribute("class")

    @allure.step("Найти заполненное поле Zip-code")
    def filled_zip_code(self) -> str:
        """
        Эта функция находит элемент по локатору и возвращает значение атрибута в виде строки
        """
        return self.driver.find_element(By.ID, "zip-code").get_attribute("class")

    @allure.step("Найти заполненное поле City")
    def filled_city(self) -> str:
        """
        Эта функция находит элемент по локатору и возвращает значение атрибута в виде строки
        """
        return self.driver.find_element(By.ID, "city").get_attribute("class")

    @allure.step("Найти заполненное поле Country")
    def filled_country(self) -> str:
        """
        Эта функция находит элемент по локатору и возвращает значение атрибута в виде строки
        """
        return self.driver.find_element(By.ID, "country").get_attribute("class")

    @allure.step("Найти заполненное поле Job position")
    def filled_job_position(self) -> str:
        """
        Эта функция находит элемент по локатору и возвращает значение атрибута в виде строки
        """
        return self.driver.find_element(By.ID, "job-position").get_attribute("class")

    @allure.step("Найти заполненное поле Company")
    def filled_company(self) -> str:
        """
        Эта функция находит элемент по локатору и возвращает значение атрибута в виде строки
        """
        return self.driver.find_element(By.ID, "company").get_attribute("class")
