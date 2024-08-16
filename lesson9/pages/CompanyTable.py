from sqlalchemy import create_engine
from sqlalchemy.sql import text


class CompanyTable:
    scripts = {
        "select": "select * from company where deleted_at is NULL",
        "delete by id": text("delete from company where id =:id_to_delete"),
        "insert new": text("insert into company(\"name\") values (:new_name)"),
        "get max id": "select MAX(\"id\") from company where deleted_at is null",
        "select by id": text("select * from company where id =:select_id and deleted_at is null")
    }

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_companies(self):
        return self.db.execute(self.scripts["select"]).fetchall()
    
    def create_company(self, name):
        self.db.execute(self.scripts["insert new"], new_name = name)
    
    def delete(self, id):
        self.db.execute(self.scripts["delete by id"], id_to_delete = id)

    def get_max_id(self):
        return self.db.execute(self.scripts["get max id"]).\
            fetchall()[0][0]
    
    def get_company_by_id(self, id):
        return self.db.execute(self.scripts["select by id"], select_id = id).fetchall()
