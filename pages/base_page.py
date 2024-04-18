import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        WebDriverWait(
            self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()
    
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    def is_visible(self, locator):
        result = True
        try:
            self.find_element_with_wait(locator)
        except TimeoutException:
            result = False
        return result

    def get_element_if_present(self, locator):
        return WebDriverWait(self.driver, timeout=3).until(EC.presence_of_element_located(locator))

    def get_element_text(self, locator):
        return self.get_element_if_present(locator).text
    
    def is_present(self, locator):
        result = True
        try:
            self.get_element_if_present(locator)
        except TimeoutException:
            result = False
        return result

    def get_list_of_elements(self, locator):
        return WebDriverWait(self.driver, timeout=10).until(EC.presence_of_all_elements_located(locator))
    
    def drag_and_drop(self, js_scripts, locator, target_locator):
        element = self.get_list_of_elements(locator)[0]
        target_element = self.driver.find_element(*target_locator)
        self.driver.execute_script(js_scripts, element, target_element)

    def wait_text_in_element(self, text, locator):
        element = WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element(locator, text)
        )
        return element