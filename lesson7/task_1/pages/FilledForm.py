from selenium.webdriver.common.by import By


class FilledForm:
     
    def __init__(self, driver):
       self.driver = driver

    def filled_first_name(self):
        return self.driver.find_element(By.ID, "first-name").get_attribute("class")

    def filled_last_name(self):
        return self.driver.find_element(By.ID, "last-name").get_attribute("class")
    
    def filled_address(self):
        return self.driver.find_element(By.ID, "address").get_attribute("class")

    def filled_mail(self):
        return self.driver.find_element(By.ID, "e-mail").get_attribute("class")

    def filled_phone(self):
        return self.driver.find_element(By.ID, "phone").get_attribute("class")

    def filled_zip_code(self):
        return self.driver.find_element(By.ID, "zip-code").get_attribute("class")

    def filled_city(self):
        return self.driver.find_element(By.ID, "city").get_attribute("class")

    def filled_country(self):
        return self.driver.find_element(By.ID, "country").get_attribute("class")

    def filled_job_position(self):
        return self.driver.find_element(By.ID, "job-position").get_attribute("class")

    def filled_company(self):
        return self.driver.find_element(By.ID, "company").get_attribute("class")
