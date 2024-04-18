from helpers import JS_SCRIPT
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage




class HomePage(BasePage):

    def click_account_button(self):
        self.click_on_element(HomePageLocators.ACCOUNT)

    def click_on_constructor(self):
        self.click_on_element(HomePageLocators.CONSTRUCTOR)

    def ingredients_block_is_visible(self):
        return self.is_visible(HomePageLocators.INGREDIENTS_BLOCK)

    def click_on_orders_feed(self):
        self.click_on_element(HomePageLocators.ORDERS_FEED)

    def click_on_first_ingredient(self):
        self.get_list_of_elements(HomePageLocators.INGREDIENTS_LIST_ELEMENTS)[0].click()

    def modal_ingredient_window_is_opened(self):
        return self.is_visible(HomePageLocators.MODAL_INGREDIENT_OPENED)
    
    def drag_and_drop_first_ingredien_to_constructor(self):
        self.drag_and_drop(JS_SCRIPT,
                           HomePageLocators.INGREDIENTS_LIST_ELEMENTS,
                           HomePageLocators.BURGER_CONSTRUCTOR)

    def get_ingredient_count(self):
        return int(self.get_list_of_elements(HomePageLocators.COUNTERS_ELEMENTS)[0].text)

    def click_on_close_button(self):
        self.get_list_of_elements(HomePageLocators.CLOSE_MODAL)[0].click()

    def click_make_order_button(self):
        self.click_on_element(HomePageLocators.MAKE_ORDER_BUTTON)

    def is_modal_order_number_present(self):
        return self.is_visible(HomePageLocators.MODAL_ORDER_NUMBER)
    
    def get_order_id(self):
        return self.get_text_from_element(HomePageLocators.ORDER_ID)