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

    assert id_emp is not None
    employee = db_emp.get_employee_by_id(id_emp)

    assert employee is not None
    assert employee["first_name"] == f_name
    assert employee["last_name"] == l_name
    assert employee["company_id"] == id_com
    assert employee["phone"] == phone
    assert employee["is_active"] == isActive

    db_emp.delete_employee(id_emp)
    db_comp.delete(company_id)


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

    assert len(db_result) == len(api_result)
    assert len(api_result) == 2

    db_emp.delete_employees_by_company_id(company_id)
    db_comp.delete(company_id)


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

    assert employee["firstName"] == f_name
    assert employee["lastName"] == l_name
    assert employee["companyId"] == id_com
    assert employee["phone"] == phone
    assert employee["isActive"] == isActive

    db_emp.delete_employee(id_emp)
    db_comp.delete(company_id)


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

    assert employee is not None
    assert employee["first_name"] == f_name
    assert employee["last_name"] == new_lname
    assert employee["company_id"] == id_com
    assert employee["phone"] == phone
    assert employee["email"] == new_mail
    assert employee["is_active"] == new_active

    db_emp.delete_employee(id_emp)
    db_comp.delete(company_id)
