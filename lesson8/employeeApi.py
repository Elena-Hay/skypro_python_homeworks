import requests


class EmployeeApi:
    def __init__(self, url) -> None:
        self.url = url
    
    def get_token(self, user='flora', password='nature-fairy'):
        creds = {
            'username': user,
            'password': password
         }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]
    
    def create_company(self, name, description):
        company = {
            "name": name,
            "description": description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/company', json=company, headers=my_headers)
        return resp.json()
    
    def get_company_list(self, params_to_add=None):
        resp = requests.get(self.url + '/company', params=params_to_add)
        return resp.json()
    
    def delete_company(self, id):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.get(self.url + '/company/delete/' + str(id), headers=my_headers)
        return resp.json()
    
    def create_employee(self, f_name, l_name, id_com, phone, isActive):
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
    
    def get_employee(self, id):
        resp = requests.get(self.url + '/employee/' + str(id))
        return resp.json()

    def get_employee_list(self, params_to_add):
        resp = requests.get(self.url + '/employee', params=params_to_add)
        return resp.json()
    
    def edit(self, id_emp, new_lname, new_mail, new_active):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        employee = {
            "lastName": new_lname,
            "email": new_mail,
            "isActive": new_active
        }
        resp = requests.patch(self.url + '/employee/' + str(id_emp), headers=my_headers, json=employee)
        return resp.json()
