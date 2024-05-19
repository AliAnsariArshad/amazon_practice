from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, locator):
        element = self.get_element(locator)
        element.click()

    def verify_page_title(self, expected_title):
        return self.driver.title.__eq__(expected_title)

    def type_into_element(self, locator, text_to_entered):
        element = self.get_element(locator)
        element.click()
        element.clear()
        element.send_keys(text_to_entered)

    def get_element(self, locator, timeout=10):
        locator_type = locator[0]
        locator_value = locator[1]
        element = None

        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.element_to_be_clickable((locator_type, locator_value)))
            return element
        except NoSuchElementException as ne:
            raise ne

    def get_elements(self, locator, timeout=20):
        locator_type = locator[0]
        locator_value = locator[1]
        elements = []

        try:
            wait = WebDriverWait(self.driver, timeout)
            elements = wait.until(EC.visibility_of_all_elements_located((locator_type, locator_value)))
            return elements
        except NoSuchElementException:
            return elements

    def retrieved_element_text_contains(self, locator, expected_text):
        element = self.get_element(locator)
        return element.text.__contains__(expected_text)

    def retrieved_element_text_equals(self, locator, expected_text):
        element = self.get_element(locator)
        return element.text.__eq__(expected_text)

    def return_and_status(self, privacy_status, first_name_status, last_name_status, email_status, telephone_status,
                          password_status):
        if privacy_status and first_name_status and last_name_status and email_status and telephone_status and password_status:
            return True
        else:
            return False

    def display_status(self, locator):
        element = self.get_element(locator)
        return element.is_displayed()

    def press_enter(self, locator):
        element = self.get_element(locator)
        element.send_keys(Keys.ENTER)

    def switch_tab(self):
        # self.driver.switch_to.window(self.driver.current_window_handle)
        window_handles = self.driver.window_handles
        for handle in window_handles:
            if handle != self.driver.current_window_handle:
                self.driver.switch_to.window(handle)
                print(self.driver.title)
                break

    def return_label_text(self, locator):
        element = self.get_element(locator)
        return element.text
