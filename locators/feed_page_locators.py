from selenium.webdriver.common.by import By

class FeedPageLocators:

    ORDERS_FEED_LIST = By.CSS_SELECTOR, '[class*="OrderFeed_list"]'
    ORDERS_ELEMENTS = By.CSS_SELECTOR, '[class*="OrderHistory_listItem"]'
    ORDER_DETAILS_MODAL_OPENED = By.CSS_SELECTOR, '[class*="Modal_modal_opened"]'
    ORDER_NUMBERS_ELEMENTS = By.XPATH, '//div[contains(@class, "OrderHistory_textBox")]//p[contains(@class, "text_type_digits")]'
    OVERALL_ORDERS_NUMBER = By.XPATH, '(//p[contains(@class, "OrderFeed_number")])[1]'
    TODAYS_ORDERS_NUMBER = By.XPATH, '(//p[contains(@class, "OrderFeed_number")])[2]'
    ORDERS_IN_PROGRESS = By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li[contains(@class, "text_type_digits-default")]'
