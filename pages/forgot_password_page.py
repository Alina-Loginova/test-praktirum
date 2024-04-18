from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage



class ForgotPasswordPage(BasePage):

    def click_restore_button(self):
        self.click_on_element(ForgotPasswordPageLocators.RESTORE_BUTTON)

    def get_restore_text(self):
       return self.get_text_from_element(ForgotPasswordPageLocators.RESTORE_TEXT)
    
    def set_email(self, text):
        self.set_text_to_element(ForgotPasswordPageLocators.EMAIL_INPUT, text)