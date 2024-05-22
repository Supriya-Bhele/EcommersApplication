from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    def add_product_to_cart(self, product_index):
        products = self.find_elements(By.CLASS_NAME, "product")
        products[product_index].find_element(By.CLASS_NAME, "add_to_cart").click()

    def checkout(self):
        self.find_element(By.ID, "checkout_button").click()

    def get_cart_items(self):
        return self.find_elements(By.CLASS_NAME, "cart_item")
