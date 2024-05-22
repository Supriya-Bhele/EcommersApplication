from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    def login(self, email, password):
        self.find_element(By.ID, "email").send_keys(email)
        self.find_element(By.ID, "password").send_keys(password)
        self.find_element(By.ID, "login_button").click()

    def get_error_message(self):
        return self.find_element(By.ID, "error_message").text
