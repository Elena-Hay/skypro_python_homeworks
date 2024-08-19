import requests
import allure


class CompanyApi:
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

    @allure.step("api. Создать компанию {name} ({description}")
    def create_company(self, name: str, description: str) -> object:
        """
        Эта функция принимает на вход название и описание компании, токен в headers.
        Возвращает JSON с информацией о созданной компании
        """
        company = {
            "name": name,
            "description": description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/company', json=company, headers=my_headers)
        return resp.json()

    @allure.step("api. Получить список компаний через API")
    def get_company_list(self, params_to_add=None) -> list:
        """
        Эта функция возвращает список компаний в формате JSON
        """
        resp = requests.get(self.url + '/company', params=params_to_add)
        return resp.json()

    @allure.step("api. Удалить компанию по {id}")
    def delete_company(self, id: int) -> object:
        """
        Эта функция принимает на вход id компании, которую необходимо удалить, токен в headers. Возвращает JSON
        """
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.get(self.url + '/company/delete/' + str(id), headers=my_headers)
        return resp.json()
