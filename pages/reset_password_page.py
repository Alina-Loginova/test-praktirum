
from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    def button_save_is_visible(self):
        return self.is_visible(ResetPasswordPageLocators.RESTORE_BUTTON)
    
    def click_on_show_password_button(self):
        self.click_on_element(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    def password_is_visible(self):
        return self.is_visible(ResetPasswordPageLocators.PASSWORD_VISIBLE)