import pytest
from selenium import webdriver
from pages.login_page import LoginPage

class TestLogin:
    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.demoblaze.com//login")
        self.login_page = LoginPage(self.driver)
        yield
        self.driver.quit()

    def test_login_positive(self, setup):
        self.login_page.login("valid@example.com", "password123")
        assert "Welcome" in self.driver.page_source

    def test_login_negative_invalid_credentials(self, setup):
        self.login_page.login("invalid@example.com", "wrongpassword")
        assert "Invalid credentials" in self.login_page.get_error_message()
