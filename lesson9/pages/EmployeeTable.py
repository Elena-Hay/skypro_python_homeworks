from sqlalchemy import create_engine
from sqlalchemy.sql import text


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

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_employee(self):
        return self.db.execute(self.scripts["select"]).fetchall()

    def delete_employee(self, id):
        self.db.execute(self.scripts["delete by id"], id_to_delete=id)

    def create_employee(self, first_name, last_name, company_id, phone, is_active):
        self.db.execute(self.scripts["insert new"], f_name=first_name, l_name=last_name, phone=phone, comp_id=company_id, active=is_active)

    def get_max_id_employee(self):
        return self.db.execute(self.scripts["get max id"]).\
            fetchall()[0][0]

    def get_employee_by_id(self, id):
        return self.db.execute(self.scripts["select by id"], select_id=id).\
            fetchone()

    def get_employees_by_company_id(self, id):
        return self.db.execute(self.scripts["select by company id"], select_id=id).\
            fetchall()

    def delete_employees_by_company_id(self, id):
        self.db.execute(self.scripts["delete by company id"], id_to_delete=id)
