import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.cart_page import CartPage

class TestShoppingCart:
    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.demoblaze.com/")
        self.home_page = HomePage(self.driver)
        self.cart_page = CartPage(self.driver)
        yield
        self.driver.quit()

    def test_add_last_product_to_cart(self, setup):
        products = self.home_page.get_products()
        last_product_index = len(products) - 1
        self.cart_page.add_product_to_cart(last_product_index)
        cart_items = self.cart_page.get_cart_items()
        assert len(cart_items) > 0
