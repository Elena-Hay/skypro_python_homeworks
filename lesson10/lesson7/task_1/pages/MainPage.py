from selenium.webdriver.common.by import By
import allure


class MainPage:
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть сайт")
    def open(self) -> None:
        """
        Эта функция открывает сайт
        """
        self.driver.get(self.url)

    @allure.step("Заполнить поле First name")
    def first_name(self, first_name) -> None:
        """
        Эта функция находит поле First name по локатору и вводит указанное значение
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys(first_name)

    @allure.step("Заполнить поле Last name")
    def last_name(self, last_name) -> None:
        """
        Эта функция находит поле Last name по локатору и вводит указанное значение
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys(last_name)

    @allure.step("Заполнить поле Address")
    def address(self, address) -> None:
        """
        Эта функция находит поле Address по локатору и вводит указанное значение
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys(address)

    @allure.step("Заполнить поле Email")
    def mail(self, mail) -> None:
        """
        Эта функция находит поле Email по локатору и вводит указанное значение
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys(mail)

    @allure.step("Заполнить поле Phone number")
    def phone(self, phone) -> None:
        """
        Эта функция находит поле Phone number по локатору и вводит указанное значение
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys(phone)

    @allure.step("Заполнить поле Zip-code")
    def zip_code(self, z_code) -> None:
        """
        Эта функция находит поле Zip-code по локатору и вводит указанное значение
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]').send_keys(z_code)

    @allure.step("Заполнить поле City")
    def city(self, city) -> None:
        """
        Эта функция находит поле City по локатору и вводит указанное значение
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys(city)

    @allure.step("Заполнить поле Country")
    def country(self, country) -> None:
        """
        Эта функция находит поле Country по локатору и вводит указанное значение
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys(country)

    @allure.step("Заполнить поле Job position")
    def job_position(self, job) -> None:
        """
        Эта функция находит поле Job position по локатору и вводит указанное значение
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys(job)

    @allure.step("Заполнить поле Company")
    def company(self, company) -> None:
        """
        Эта функция находит поле Company по локатору и вводит указанное значение
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys(company)

    @allure.step("Нажать на кнопку Submit")
    def submit(self) -> None:
        """
        Эта функция находит кнопку Submit по локатору и кликает на нее
        """
        self.driver.find_element(By.CSS_SELECTOR, '.btn-outline-primary').click()
