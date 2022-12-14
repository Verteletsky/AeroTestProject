from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium import webdriver
import math
from selenium.common.exceptions import NoAlertPresentException  # в начале файла
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, 3).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def click_button_to_basket(self):
        btn_basket = self.browser.find_element(*ProductPageLocators.ADD_BUTTON_BASKET)
        btn_basket.click()
        # self.solve_quiz_and_get_code()

    def should_not_be_success_message(self):
        # is_not_element_present: упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый.
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        # is_disappeared: будет ждать до тех пор, пока элемент не исчезнет.
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Not success message is disappered"

    def check_product(self):
        self.check_name_product()
        # self.check_price_product()

    def check_name_product(self):
        added_title_product = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)

        print("========================")
        print(added_title_product.text)
        print("========================")

        actual_title_product = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE_ACTUAL)

        assert added_title_product.text == actual_title_product.text

    def check_price_product(self):
        added_price_product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)

        print("========================")
        print(added_price_product.text)
        print("========================")

        actual_price_product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ACTUAL)

        assert added_price_product.text == actual_price_product.text
