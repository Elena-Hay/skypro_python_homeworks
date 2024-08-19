import allure
from pages.CompanyApi import CompanyApi
from pages.EmployeeApi import EmployeeApi
from pages.CompanyTable import CompanyTable
from pages.EmployeeTable import EmployeeTable


db_connection_string = "postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0"
api_url = "https://x-clients-be.onrender.com"
api_comp = CompanyApi(api_url)
api_emp = EmployeeApi(api_url)
db_comp = CompanyTable(db_connection_string)
db_emp = EmployeeTable(db_connection_string)


@allure.feature("CREATE")
@allure.title("Добавление нового сотрудника в компанию")
@allure.description("Тест проверяет. что созданный через API сотрудник отображается в базе данных")
@allure.severity("blocker")
def test_add_new_employee():
    name = "Клик"
    db_comp.create_company(name)
    company_id = db_comp.get_max_id()

    f_name = "Елена"
    l_name = "Орлова"
    id_com = company_id
    phone = "+79576847731"
    isActive = True
    new_emp = api_emp.create_employee(f_name, l_name, id_com, phone, isActive)
    id_emp = new_emp["id"]

    with allure.step("Проверить, что id созданного сотрудника не пустой"):
        assert id_emp is not None
    employee = db_emp.get_employee_by_id(id_emp)

    with allure.step("Проверить поля нового сотрудника. Корректность заполнения"):
        assert employee is not None
        assert employee["first_name"] == f_name
        assert employee["last_name"] == l_name
        assert employee["company_id"] == id_com
        assert employee["phone"] == phone
        assert employee["is_active"] == isActive

    db_emp.delete_employee(id_emp)
    db_comp.delete(company_id)


@allure.feature("READ")
@allure.title("Получение списка сотрудников компании")
@allure.description("Тест проверяет эквивалентность списков сотрудников, полученных через API и базу данных")
@allure.severity("blocker")
def test_get_employee_list():
    name = "Клик"
    db_comp.create_company(name)
    company_id = db_comp.get_max_id()

    f_name = "Елена"
    l_name = "Орлова"
    phone = "+79576847731"
    isActive = True
    db_emp.create_employee(f_name, l_name, company_id, phone, isActive)
    db_emp.create_employee(f_name, l_name, company_id, phone, isActive)

    db_result = db_emp.get_employees_by_company_id(company_id)
    api_result = api_emp.get_employee_list(params_to_add={'company': company_id})

    with allure.step("Проверить, что список, полученный по API, равен списку, полученному из БД"):
        assert len(db_result) == len(api_result)
    with allure.step("Проверить, что длина списка равна 2"):
        assert len(api_result) == 2

    db_emp.delete_employees_by_company_id(company_id)
    db_comp.delete(company_id)



@allure.feature("READ")
@allure.title("Получение сотрудника по id")
@allure.description("Тест проверяет соответствие сотрудника, запрошенного по id через API, искомому в базе данных")
@allure.severity("blocker")
def test_get_employee():
    name = "Клик"
    db_comp.create_company(name)
    company_id = db_comp.get_max_id()

    f_name = "Елена"
    l_name = "Орлова"
    id_com = company_id
    phone = "+79576847731"
    isActive = True
    db_emp.create_employee(f_name, l_name, id_com, phone, isActive)
    id_emp = db_emp.get_max_id_employee()

    employee = api_emp.get_employee(id_emp)

    with allure.step("Проверить, что поля найденного сотрудника через API соответствуют полям созданного сотрудника через БД"):
        assert employee["firstName"] == f_name
        assert employee["lastName"] == l_name
        assert employee["companyId"] == id_com
        assert employee["phone"] == phone
        assert employee["isActive"] == isActive

    db_emp.delete_employee(id_emp)
    db_comp.delete(company_id)


@allure.feature("UPDATE")
@allure.title("Изменение информации о сотруднике")
@allure.description("Тест проверяет обновление информации о сотруднике в базе данных после внесения изменений через API")
@allure.severity("blocker")
def test_edit_employee():
    name = "Клик"
    db_comp.create_company(name)
    company_id = db_comp.get_max_id()

    f_name = "Елена"
    l_name = "Орлова"
    id_com = company_id
    phone = "+79576847731"
    isActive = True
    db_emp.create_employee(f_name, l_name, id_com, phone, isActive)
    id_emp = db_emp.get_max_id_employee()

    new_lname = "Котова"
    new_mail = "kotova@golos.ru"
    new_active = False
    api_emp.edit(id_emp, new_lname, new_mail, new_active)

    employee = db_emp.get_employee_by_id(id_emp)

    with allure.step("Проверить, что информация о сотруднике соответсвует изменениям"):
        assert employee is not None
        assert employee["first_name"] == f_name
        assert employee["last_name"] == new_lname
        assert employee["company_id"] == id_com
        assert employee["phone"] == phone
        assert employee["email"] == new_mail
        assert employee["is_active"] == new_active

    db_emp.delete_employee(id_emp)
    db_comp.delete(company_id)
