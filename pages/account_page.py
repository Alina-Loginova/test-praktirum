from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage



class AccountPage(BasePage):
    def profile_is_visible(self):
        return self.is_visible(AccountPageLocators.ACCOUNT_PROFILE)

    def click_orders_history(self):
        self.click_on_element(AccountPageLocators.ORDERS_HISTORY)

    def orders_is_visible(self):
        return self.is_present(AccountPageLocators.ORDERS_LIST)

    def click_on_exit(self):
        self.click_on_element(AccountPageLocators.EXIT_BUTTON)

    def get_first_order_number(self):
        return self.get_list_of_elements(AccountPageLocators.ACCOUNT_ORDERS_ELEMENTS)[0].text
