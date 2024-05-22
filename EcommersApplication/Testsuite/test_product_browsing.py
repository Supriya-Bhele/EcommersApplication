import pytest
from selenium import webdriver
from pages.home_page import HomePage

class TestProductBrowsing:
    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.demoblaze.com/")
        self.home_page = HomePage(self.driver)
        yield
        self.driver.quit()

    def test_products_displayed(self, setup):
        products = self.home_page.get_products()
        assert len(products) > 0

    def test_navigate_to_category(self, setup):
        self.home_page.navigate_to_category("Electronics")
        assert "Electronics" in self.driver.title
