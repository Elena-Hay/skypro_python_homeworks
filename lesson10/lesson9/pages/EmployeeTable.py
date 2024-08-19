from sqlalchemy import create_engine
from sqlalchemy.sql import text
import allure


class EmployeeTable:
    scripts = {
        "select": "select * from employee",
        "delete by id": text("delete from employee where id =:id_to_delete"),
        "insert new": text("insert into employee(\"first_name\", \"last_name\", \"phone\", \"company_id\", \"is_active\") values (:f_name, :l_name, :phone, :comp_id, :active)"),
        "get max id": "select MAX(\"id\") from employee",
        "select by id": text("select * from employee where id =:select_id"),
        "select by company id": text("select * from employee where company_id =:select_id"),
        "delete by company id": text("delete from employee where company_id =:id_to_delete")
    }

    def __init__(self, connection_string: str) -> None:
        self.db = create_engine(connection_string)

    @allure.step("БД. Запросить список сотрудников")
    def get_employee(self) -> list:
        """
        Эта функция отправляет SELECT-запрос в базу данных, возвращает список записей
        """
        return self.db.execute(self.scripts["select"]).fetchall()

    @allure.step("БД. Удалить сотрудника по {id}")
    def delete_employee(self, id: int) -> None:
        """
        Эта функция принимает id сотрудника, отправляет DELETE-запрос в базу данных
        """
        self.db.execute(self.scripts["delete by id"], id_to_delete=id)

    @allure.step("БД. Создать сотрудника: {first_name}, {last_name}, {company_id}, {phone}, {is_active}")
    def create_employee(self, first_name: str, last_name: str, company_id: int, phone: str, is_active: bool) -> None:
        """
        Эта функция принимает на вход параметры: имя и фамилия сотрудника, id компании, телефон,
        (де)активация сотрудника. Отправляет INSERT-запрос в базу данных
        """
        self.db.execute(self.scripts["insert new"], f_name=first_name, l_name=last_name, phone=phone, comp_id=company_id, active=is_active)

    @allure.step("БД. Запросить сотрудника по максимальному id")
    def get_max_id_employee(self) -> int:
        """
        Эта функция отправляет SELECT-запрос в базу данных, возвращает запись с максимальным id сотрудника
        """
        return self.db.execute(self.scripts["get max id"]).\
            fetchall()[0][0]

    @allure.step("БД. Запросить сотрудника по {id}")
    def get_employee_by_id(self, id: int) -> dict:
        """
        Эта функция принимает на вход id сотрудника, отправляет SELECT-запрос в базу данных, возвращает запись
        """
        return self.db.execute(self.scripts["select by id"], select_id=id).\
            fetchone()

    @allure.step("БД. Запросить список сотрудников по {id} компании")
    def get_employees_by_company_id(self, id: int) -> list:
        """
        Эта функция принимает на вход id компании, отправляет SELECT-запрос в базу данных,
        возвращает список записей
        """
        return self.db.execute(self.scripts["select by company id"], select_id=id).\
            fetchall()

    @allure.step("БД. Удалить сотрудников по {id} компании")
    def delete_employees_by_company_id(self, id: int) -> None:
        """
        Эта функция принимает на вход id компании, отправляет DELETE-запрос в базу данных
        """
        self.db.execute(self.scripts["delete by company id"], id_to_delete=id)
