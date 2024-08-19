from selenium import webdriver

from pages.CalcPage import CalcPage
from pages.Result import Result
import allure


@allure.feature("Вычисления")
@allure.title("Калькулятор")
@allure.description("Тест проверяет правильность вычисления калькулятора")
@allure.severity("blocker")
def test_calculator():
    browser = webdriver.Chrome()

    calcPage = CalcPage(browser)
    calcPage.open()
    calcPage.delay(45)
    calcPage.sum()
    calcPage.wait(60)

    result = Result(browser)
    result.res()

    with allure.step("Проверить, что результат вычисления равен 15"):
        result.res() == "15"
    with allure.step("Закрыть браузер"):
        browser.quit()
