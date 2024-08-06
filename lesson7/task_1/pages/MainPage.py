from selenium.webdriver.common.by import By


class MainPage:
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def __init__(self, driver):
        self.driver = driver      

    def open(self):
        self.driver.get(self.url)

    def first_name(self, first_name):
        self.driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys(first_name)

    def last_name(self, last_name):
        self.driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys(last_name)
    
    def address(self, address):
        self.driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys(address)

    def mail(self, mail):
        self.driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys(mail)

    def phone(self, phone):
        self.driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys(phone)

    def zip_code(self, z_code):
        self.driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]').send_keys(z_code)

    def city(self, city):
        self.driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys(city)

    def country(self, country):
        self.driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys(country)

    def job_position(self, job):
        self.driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys(job)

    def company(self, company):
        self.driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys(company)

    def submit(self):
        self.driver.find_element(By.CSS_SELECTOR, '.btn-outline-primary').click()
