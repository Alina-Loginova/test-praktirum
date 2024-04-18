import allure
import pytest

from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
from urls import FORGOT_PASSWORD, LOGIN

@allure.story('Восстановление пароля')
class TestRecoveryPasswordPage:

    @allure.title('Успешный переход на страницу восстановления')
    @pytest.mark.parametrize(
        "web_driver",
        ['driver_chrome', 'driver_firefox']
    )
    def test_go_to_recovery_page(self, request, web_driver):
        driver = request.getfixturevalue(web_driver)
        login_page = LoginPage(driver)
        login_page.get_url(LOGIN)
        login_page.click_reset_password()
        forgot_password_page = ForgotPasswordPage(driver)
        assert forgot_password_page.get_restore_text() == 'Восстановление пароля'


    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    @pytest.mark.parametrize(
        "web_driver",
        ['driver_chrome', 'driver_firefox']
    )
    def test_enter_email_and_go_to_reset_page(self, request, web_driver, register_new_user):
        driver = request.getfixturevalue(web_driver)
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.get_url(FORGOT_PASSWORD)
        forgot_password_page.set_email(register_new_user['email'])
        forgot_password_page.click_restore_button()
        reset_password_page = ResetPasswordPage(driver)
        assert reset_password_page.button_save_is_visible()

    @allure.title('Клик по кнопке показать/скрыть пароль')
    @pytest.mark.parametrize(
        "web_driver",
        ['driver_chrome', 'driver_firefox']
    )
    def test_click_on_show_password(self, request, web_driver, register_new_user):
        driver = request.getfixturevalue(web_driver)
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.get_url(FORGOT_PASSWORD)
        forgot_password_page.set_email(register_new_user['email'])
        forgot_password_page.click_restore_button()
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.click_on_show_password_button()
        assert reset_password_page.password_is_visible()