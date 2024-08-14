import requests


class CompanyApi:
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
