import requests
import allure


class EmployeeApi:
    def __init__(self, url: str) -> None:
        self.url = url

    @allure.step("api. Получить токен авторизации {user}:{password}")
    def get_token(self, user: str = 'flora', password: str = 'nature-fairy') -> str:
        """
        Эта функция принимает на вход имя пользователя и пароль, возвращает токен для авторизации
        """
        creds = {
            'username': user,
            'password': password
         }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]

    @allure.step("api. Создать сотрудника c id компании в параметрах: {f_name}, {l_name}, {id_com}, {phone}, {isActive}")
    def create_employee(self, f_name: str, l_name: str, id_com: int, phone: str, isActive: bool) -> object:
        """
        Эта функция принимает на вход параметры: имя и фамилия сотрудника, id компании, телефон,
        (де)активация сотрудника, токен в headers.
        Возвращает JSON с информацией о созданном сотруднике
        """
        employee = {
            "firstName": f_name,
            "lastName": l_name,
            "companyId": id_com,
            "phone": phone,
            "isActive": isActive
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee', json=employee, headers=my_headers)
        return resp.json()

    @allure.step("api. Получить сотрудника по {id}")
    def get_employee(self, id: int) -> object:
        """
        Эта функция принимает на вход id сотрудника, возвращает JSON с информацией о сотруднике
        """
        resp = requests.get(self.url + '/employee/' + str(id))
        return resp.json()

    @allure.step("api. Получить список всех сотрудников")
    def get_employee_list(self, params_to_add: dict) -> list:
        """
        Эта функция принимает параметры запроса params_to_add={'company': company_id},
        возвращает список сотрудников в формате JSON
        """
        resp = requests.get(self.url + '/employee', params=params_to_add)
        return resp.json()

    @allure.step("api. Изменить информацию о сотруднике: {id_emp}, {new_lname}, {new_mail}, {new_active}")
    def edit(self, id_emp: int, new_lname: str, new_mail: str, new_active: bool) -> object:
        """
        Эта функция принимает на вход параметры, которые необходимо изменить: имя и фамилия сотрудника,
        id компании, телефон, (де)активация сотрудника, токен в headers. Возвращает JSON с измененными данными
        """
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        employee = {
            "lastName": new_lname,
            "email": new_mail,
            "isActive": new_active
        }
        resp = requests.patch(self.url + '/employee/' + str(id_emp), headers=my_headers, json=employee)
        return resp.json()
