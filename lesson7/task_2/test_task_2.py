from selenium import webdriver

from pages.CalcPage import CalcPage
from pages.Result import Result


def test_calculator():
    browser = webdriver.Chrome()

    calcPage = CalcPage(browser)
    calcPage.open()
    calcPage.delay(45)
    calcPage.sum()
    calcPage.wait(60)

    result = Result(browser)
    result.res()

    assert result.res() == "15"
    browser.quit()
