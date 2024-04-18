from selenium.webdriver.common.by import By

class ForgotPasswordPageLocators:
    RESTORE_TEXT = By.XPATH, "//*[contains(text(),'Восстановление пароля')]"
    RESTORE_BUTTON = By.XPATH, '//button[text()="Восстановить"]'
    EMAIL_INPUT= By.CSS_SELECTOR, 'input[name="name"]'