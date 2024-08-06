from selenium import webdriver

from pages.AuthPage import AuthPage
from pages.ProductsPage import Products
from pages.CartPage import Cart
from pages.YourInformationPage import Informations
from pages.OverviewPage import Overview


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

    assert res.result() == "Total: $58.29"
    browser.quit()
