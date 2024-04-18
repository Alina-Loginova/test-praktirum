from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage
from selenium.common import TimeoutException



class FeedPage(BasePage):

    def is_orders_feed_list_visible(self):
        return self.is_present(FeedPageLocators.ORDERS_FEED_LIST)

    def click_on_first_order(self):
        self.get_list_of_elements(FeedPageLocators.ORDERS_ELEMENTS)[0].click()

    def is_order_details_modal_opened(self):
        return self.is_present(FeedPageLocators.ORDER_DETAILS_MODAL_OPENED)

    def get_list_order_numbers(self):
        order_numbers_elements = self.get_list_of_elements(FeedPageLocators.ORDER_NUMBERS_ELEMENTS)
        order_numbers = [order_element.text for order_element in order_numbers_elements]
        return order_numbers

    def get_overall_orders_number(self):
        return int(self.get_element_text(FeedPageLocators.OVERALL_ORDERS_NUMBER))

    def is_overall_order_counter_increased(self, before_order: int):
        result = True
        try:
            self.wait_text_in_element(str(before_order+1), FeedPageLocators.OVERALL_ORDERS_NUMBER)
        except TimeoutException:
            result = False
        return result

    def get_todays_orders_number(self):
        return int(self.get_element_text(FeedPageLocators.TODAYS_ORDERS_NUMBER))

    def is_todays_order_counter_increased(self, before_order: int):
        result = True
        try:
            self.wait_text_in_element(str(before_order+1), FeedPageLocators.TODAYS_ORDERS_NUMBER)
        except TimeoutException:

            result = False
        return result

    def is_order_in_progress(self, order_number):
        result = True
        try:
            self.wait_text_in_element(str(f'0{order_number}'), FeedPageLocators.ORDERS_IN_PROGRESS)
        except TimeoutException:
            result = False
        return result

