import allure
import pytest

from pages.account_page import AccountPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from urls import LOGIN


@allure.story('Личный кабинет')
class TestRecoveryPasswordPage:

    @allure.title('Переход по клику на «Личный кабинет»')
    @pytest.mark.parametrize(
        "web_driver",
        ['driver_chrome', 'driver_firefox']
    )
    def test_go_to_account(self, request, web_driver, register_new_user):
        driver = request.getfixturevalue(web_driver)
        login_page = LoginPage(driver)
        login_page.get_url(LOGIN)
        login_page.click_login_with_credentials(register_new_user['email'], register_new_user['password'])

        home_page = HomePage(driver)
        home_page.click_account_button()

        account_page = AccountPage(driver)
        assert account_page.profile_is_visible()

    @allure.title('Открытие истории заказов')
    @pytest.mark.parametrize(
        "web_driver",
        ['driver_chrome', 'driver_firefox']
    )
    def test_go_to_orders_history(self, request, web_driver, register_new_user):
        driver = request.getfixturevalue(web_driver)
        login_page = LoginPage(driver)
        login_page.get_url(LOGIN)
        login_page.click_login_with_credentials(register_new_user['email'], register_new_user['password'])

        home_page = HomePage(driver)
        home_page.click_account_button()

        account_page = AccountPage(driver)
        account_page.click_orders_history()
        assert account_page.orders_is_visible()

    @allure.title('Выход из аккаунта')
    @pytest.mark.parametrize(
        "web_driver",
        ['driver_chrome', 'driver_firefox']
    )
    def test_go_to_logout(self, request, web_driver, register_new_user):
        driver = request.getfixturevalue(web_driver)
        login_page = LoginPage(driver)
        login_page.get_url(LOGIN)
        login_page.click_login_with_credentials(register_new_user['email'], register_new_user['password'])

        home_page = HomePage(driver)
        home_page.click_account_button()

        account_page = AccountPage(driver)
        account_page.click_on_exit()
        assert login_page.is_login_button_present()