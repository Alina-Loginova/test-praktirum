from selenium.webdriver.common.by import By

class ResetPasswordPageLocators:
    RESTORE_BUTTON = By.XPATH, '//button[text()="Сохранить"]'
    SHOW_PASSWORD_BUTTON = By.CSS_SELECTOR, '.input__icon-action > svg[xmlns="http://www.w3.org/2000/svg"]'
    PASSWORD_VISIBLE = By.CSS_SELECTOR, '.input_status_active'