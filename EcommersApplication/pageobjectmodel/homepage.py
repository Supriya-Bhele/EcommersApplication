from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    def get_products(self):
        return self.find_elements(By.CLASS_NAME, "product")

    def navigate_to_category(self, category_name):
        self.find_element(By.LINK_TEXT, category_name).click()
