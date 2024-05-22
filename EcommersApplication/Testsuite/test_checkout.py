import pytest
from selenium import webdriver
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestCheckout:
    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.demoblaze.com/")
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        yield
        self.driver.quit()

    def test_checkout_positive(self, setup):
        self.cart_page.add_product_to_cart(0)
        self.cart_page.checkout()
        assert "Order Confirmation" in self.driver.page_source

    def test_checkout_negative_no_products(self, setup):
        self.driver.get("https://www.demoblaze.com/")
        self.cart_page.checkout()
        assert "Your cart is empty" in self.driver.page_source
