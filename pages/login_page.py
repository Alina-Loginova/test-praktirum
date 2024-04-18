from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def click_reset_password(self):
        self.click_on_element(LoginPageLocators.FORGOT_PASSWORD)

    def click_login_with_credentials(self, email, password):
        self.set_text_to_element(LoginPageLocators.INPUT_EMAIL_FIELD, email)
        self.set_text_to_element(LoginPageLocators.INPUT_PASSWORD_FIELD, password)
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON)

    def is_login_button_present(self):
        return self.is_visible(LoginPageLocators.LOGIN_BUTTON)