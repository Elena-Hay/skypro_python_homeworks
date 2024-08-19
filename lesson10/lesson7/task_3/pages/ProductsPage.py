from selenium.webdriver.common.by import By
import allure


class Products:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Добавить товары в корзину")
    def add_to_cart(self) -> None:
        """
        Эта функция добавляет товары в корзину: находит кнопку Add to cart по локатору
        у каждого продукта и кликает на них
        """
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

    @allure.step("Перейти в корзину")
    def cart(self) -> None:
        """
        Эта функция по локатору находит значок корзины и кликает на него
        """
        self.driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()
