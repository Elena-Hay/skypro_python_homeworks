from sqlalchemy import create_engine
from sqlalchemy.sql import text
import allure


class CompanyTable:
    scripts = {
        "select": "select * from company where deleted_at is NULL",
        "delete by id": text("delete from company where id =:id_to_delete"),
        "insert new": text("insert into company(\"name\") values (:new_name)"),
        "get max id": "select MAX(\"id\") from company where deleted_at is null",
        "select by id": text("select * from company where id =:select_id and deleted_at is null")
    }

    def __init__(self, connection_string: str) -> None:
        self.db = create_engine(connection_string)

    @allure.step("БД. Запросить список компаний")
    def get_companies(self) -> list:
        """
        Эта функция отправляет SELECT-запрос в базу данных, возвращает список записей
        """
        return self.db.execute(self.scripts["select"]).fetchall()

    @allure.step("БД. Создать компанию с названием {name}")
    def create_company(self, name: str) -> None:
        """
        Эта функция принимает на вход название компании и отправляет INSERT-запрос в базу данных
        """
        self.db.execute(self.scripts["insert new"], new_name=name)

    @allure.step("БД. Удалить компанию по {id}")
    def delete(self, id: int) -> None:
        """
        Эта функция принимает на вход id компании, отправляет DELETE-запрос в базу данных
        """
        self.db.execute(self.scripts["delete by id"], id_to_delete=id)

    @allure.step("БД. Запросить компанию с максимальным id")
    def get_max_id(self) -> list:
        """
        Эта функция отправляет SELECT-запрос в базу данных, возвращает запись с максимальным id компании
        """
        return self.db.execute(self.scripts["get max id"]).\
            fetchall()[0][0]

    @allure.step("БД. Запросить компанию по {id}")
    def get_company_by_id(self, id: int) -> list:
        """
        Эта функция принимает на вход id компании, отправляет SELECT-запрос в базу данных,
        возвращает запись с искомым id
        """
        return self.db.execute(self.scripts["select by id"], select_id=id).fetchall()
