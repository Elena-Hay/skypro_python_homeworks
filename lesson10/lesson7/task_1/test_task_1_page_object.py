from selenium import webdriver

from pages.MainPage import MainPage
from pages.FilledForm import FilledForm
import allure


@allure.feature("Заполнение полей")
@allure.title("Отправка заполненной формы")
@allure.description("Тест проверяет, что поля формы верно подсвечены в зависимости от заполнения/незаполнения")
@allure.severity("critical")
def test_form():
    browser = webdriver.Chrome()

    mainPage = MainPage(browser)
    mainPage.open()
    mainPage.first_name("Иван")
    mainPage.last_name("Петров")
    mainPage.address("Ленина, 55-3")
    mainPage.mail("test@skypro.com")
    mainPage.phone("+7985899998787")
    mainPage.zip_code("")
    mainPage.city("Москва")
    mainPage.country("Россия")
    mainPage.job_position("QA")
    mainPage.company("SkyPro")
    mainPage.submit()

    f_form = FilledForm(browser)

    with allure.step("Проверить, что поле Zip-code подсвечено красным цветом"):
        assert "danger" in f_form.filled_zip_code()
    with allure.step("Проверить, что все поля формы, кроме поля Zip-code, подсвечены зеленым цветом"):
        assert "success" in f_form.filled_first_name()
        assert "success" in f_form.filled_last_name()
        assert "success" in f_form.filled_address()
        assert "success" in f_form.filled_mail()
        assert "success" in f_form.filled_phone()
        assert "success" in f_form.filled_city()
        assert "success" in f_form.filled_country()
        assert "success" in f_form.filled_job_position()
        assert "success" in f_form.filled_company()
    with allure.step("Закрыть браузер"):
        browser.quit()
