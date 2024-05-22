import pytest
from selenium import webdriver
from pages.signup_page import SignupPage

class TestSignup:
    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.demoblaze.com/signup")
        self.signup_page = SignupPage(self.driver)
        yield
        self.driver.quit()

    def test_signup_positive(self, setup):
        self.signup_page.signup("testuser", "test@example.com", "password123")
        assert "Welcome" in self.driver.page_source

    def test_signup_negative_existing_email(self, setup):
        self.signup_page.signup("testuser", "existing@example.com", "password123")
        assert "Email already exists" in self.signup_page.get_error_message()
