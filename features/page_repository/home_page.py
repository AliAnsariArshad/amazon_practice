import pdb
import time

from selenium.webdriver.common.by import By

from features.page_repository.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    TXTBOX_SEARCH = (By.CSS_SELECTOR, "#twotabsearchtextbox")
    LBL_RESULT_LIST = (By.CSS_SELECTOR, ".a-size-mini .a-link-normal .a-size-medium ")
    BTN_ADD_TO_CART = (By.XPATH, "//div[@id='desktop_qualifiedBuyBox']//input[@id='add-to-cart-button' and @title='Add to Shopping Cart']")
    LBL_PRICE = (By.CSS_SELECTOR, "#corePrice_feature_div  .a-price-whole")
    BTN_CART = (By.CSS_SELECTOR, "#attach-sidesheet-view-cart-button .a-button-inner")
    LBL_PRODUCT_PRICE = (By.XPATH, "//div[@data-name='Active Items']//span[contains(@class,'sc-product-price')]")
    LBL_SUB_TOTAL = (By.CSS_SELECTOR, "#sc-subtotal-label-activecart+#sc-subtotal-amount-activecart .a-size-medium")

    def enter_in_search_box(self, text):
        self.type_into_element(self.TXTBOX_SEARCH, text)
        self.press_enter(self.TXTBOX_SEARCH)

    def select_item(self, item_number):
        product_list = self.get_elements(self.LBL_RESULT_LIST)
        if item_number.lower() == "first":
            product_list[0].click()
        elif item_number.lower() == "second":
            product_list[1].click()
        self.switch_tab()

        # time.sleep(20)

    def add_to_cart(self):
        # add_to_cart = self.get_elements(self.BTN_ADD_TO_CART)
        # if len(add_to_cart) == 0:
        #     add_to_cart[0].click()
        # elif len(add_to_cart) > 0:
        #     add_to_cart[1].click()
        self.click_on_element(self.BTN_ADD_TO_CART)

    def click_on_cart_button(self):
        self.click_on_element(self.BTN_CART)

    def return_product_price(self):
        return self.return_label_text(self.LBL_PRICE)

    def return_subtotal(self):
        return self.return_label_text(self.LBL_SUB_TOTAL)

    def return_cart_product_price(self):
        return self.return_label_text(self.LBL_PRODUCT_PRICE)
