from employeeApi import EmployeeApi


api = EmployeeApi("https://x-clients-be.onrender.com")


def test_add_new_employee_id():
    #Создание компании
    name = "ИРИС"
    description = "Лучшая компания"
    result = api.create_company(name, description)
    new_id = result["id"]

    #Создание сотрудника в компании
    f_name = "Дария"
    l_name = "Пязанова"
    id_com = new_id
    phone = "+79576846531"
    isActive = True
    new_emp = api.create_employee(f_name, l_name, id_com, phone, isActive)
    id_emp = new_emp["id"]

    #Получение сотрудника по id
    new_employee = api.get_employee(id_emp)
    
    assert new_employee["id"] == id_emp
    assert new_employee["firstName"] == f_name
    assert new_employee["lastName"] == l_name
    assert new_employee["companyId"] == id_com
    assert new_employee["phone"] == phone
    assert new_employee["isActive"] == isActive

    #Удаление созданной компании вместе с сотрудниками
    edited_company = api.delete_company(new_id)
    assert edited_company["id"] == new_id
    assert edited_company["name"] == name
    assert edited_company["description"] == description
    assert edited_company["isActive"] == True

def test_get_list_employee():
    #Создание компании
    name = "Ранетка"
    description = "Компания для интересных людей"
    result = api.create_company(name, description)
    new_id = result["id"]

    #Получение списка сотрудников компании
    body = api.get_employee_list(params_to_add={'company': new_id})
    len_before = len(body)

    #Создание сотрудника №1 в компании
    f_name = "Светлана"
    l_name = "Минова"
    id_com = new_id
    phone = "+79578906639"
    isActive = True
    api.create_employee(f_name, l_name, id_com, phone, isActive)
    
    #Создание сотрудника №2 в компании
    f_name = "Игорь"
    l_name = "Долгов"
    id_com = new_id
    phone = "+79438902230"
    isActive = True
    api.create_employee(f_name, l_name, id_com, phone, isActive)

    #Получение списка сотрудников компании
    body_2 = api.get_employee_list(params_to_add={'company': new_id})
    len_after = len(body_2)
    
    #Проверка, что созданные сотрудники появились в списке сотрудников компании
    assert len_after - len_before == 2

    #Удаление созданной компании вместе с сотрудниками
    edited_company = api.delete_company(new_id)
    assert edited_company["id"] == new_id
    assert edited_company["name"] == name
    assert edited_company["description"] == description
    assert edited_company["isActive"] == True

def test_edit_employee():
    #Создание компании
    name = "Марсианин"
    description = "Компания для лучших"
    result = api.create_company(name, description)
    new_id = result["id"]

    #Создание сотрудника в компании
    f_name = "Кристина"
    l_name = "Сумина"
    id_com = new_id
    phone = "+79575566539"
    isActive = True
    new_emp = api.create_employee(f_name, l_name, id_com, phone, isActive)
    id_emp = new_emp["id"]

    #Изменение информации о сотруднике
    new_lname = "Котова"
    new_mail = "kotova@golos.ru"
    new_active = False
    edited = api.edit(id_emp, new_lname, new_mail, new_active)

    assert edited["id"] == id_emp
    
    #Получение сотрудника по id
    employee = api.get_employee(id_emp)
    
    assert employee["lastName"] == new_lname
    assert employee["email"] == new_mail
    assert employee["isActive"] == False

    #Удаление созданной компании вместе с сотрудниками
    edited_company = api.delete_company(new_id)
    assert edited_company["id"] == new_id
    assert edited_company["name"] == name
    assert edited_company["description"] == description
    assert edited_company["isActive"] == True
