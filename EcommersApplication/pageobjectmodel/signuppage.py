from selenium.webdriver.common.by import By
from .base_page.py import BasePage


class SignupPage(BasePage):
    def signup(self, username, email, password):
        self.find_element(By.ID, "username").send_keys(username)
        self.find_element(By.ID, "email").send_keys(email)
        self.find_element(By.ID, "password").send_keys(password)
        self.find_element(By.ID, "signup_button").click()

    def get_error_message(self):
        return self.find_element(By.ID, "error_message").text
