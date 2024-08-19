from selenium import webdriver

from pages.AuthPage import AuthPage
from pages.ProductsPage import Products
from pages.CartPage import Cart
from pages.YourInformationPage import Informations
from pages.OverviewPage import Overview
import allure


@allure.feature("Итог покупок")
@allure.title("Магазин")
@allure.description("Тест проверяет правильность отображения итоговой суммы покупок")
@allure.severity("blocker")
def test_buy():
    browser = webdriver.Chrome()

    authPage = AuthPage(browser)
    authPage.open()
    authPage.authorization("standard_user", "secret_sauce")
    authPage.button()

    products = Products(browser)
    products.add_to_cart()
    products.cart()

    cart = Cart(browser)
    cart.check()

    info = Informations(browser)
    info.first_name("Елена")
    info.last_name("Хайбулкина")
    info.postal_code("432029")
    info.button_continue()

    res = Overview(browser)
    res.result()

    with allure.step("Проверить, что итоговая сумма равна $58.29"):
        assert res.result() == "Total: $58.29"
    with allure.step("Закрыть браузер"):
        browser.quit()
