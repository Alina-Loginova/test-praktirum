from selenium.webdriver.common.by import By

class LoginPageLocators:
    FORGOT_PASSWORD = By.CSS_SELECTOR, '[href="/forgot-password"]'
    INPUT_EMAIL_FIELD = By.CSS_SELECTOR, 'input[type="text"]'
    INPUT_PASSWORD_FIELD = By.CSS_SELECTOR, 'input[type="password"]'
    LOGIN_BUTTON = By.XPATH, '//button[text()="Войти"]'
    