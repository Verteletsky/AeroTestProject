from .base_page import BasePage
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(By.CSS_SELECTOR, ".basket-items"), \
            "Empty basket"

    def should_be_message_empty_basket(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#content_inner p"), \
            "Element exist!"
