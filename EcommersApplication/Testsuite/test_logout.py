import pytest
from selenium import webdriver
from pages.home_page import HomePage

class TestLogout:
    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.demoblaze.com/")
        self.home_page = HomePage(self.driver)
        yield
        self.driver.quit()

    def test_logout_positive(self, setup):
        self.home_page.logout()
        assert "Login" in self.driver.page_source
