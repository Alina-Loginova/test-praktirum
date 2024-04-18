from selenium.webdriver.common.by import By

class AccountPageLocators:
    ACCOUNT_PROFILE = By.CSS_SELECTOR, '[href="/account/profile"]'
    ORDERS_HISTORY = By.CSS_SELECTOR, '[href="/account/order-history"]'
    ORDERS_LIST = By.CSS_SELECTOR, 'ul[class*="OrderHistory_profileList"]'
    EXIT_BUTTON = By.XPATH, '//button[text()="Выход"]'
    ACCOUNT_ORDERS_ELEMENTS = By.XPATH, '//div[contains(@class, "OrderHistory_textBox")]//p[contains(@class, "text_type_digits")]'