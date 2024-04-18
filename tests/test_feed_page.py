import time
import allure
import pytest

from pages.account_page import AccountPage
from pages.feed_page import FeedPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from urls import ACCOUNT, FEED_PAGE, LOGIN


@allure.story('Лента заказов')
class TestFeedPage:

    @allure.title('Нажатие на номер заказа открывает модальное окно с деталями заказа')
    @pytest.mark.parametrize(
        "web_driver",
        ['driver_chrome', 'driver_firefox']
    )
    def test_click_order_open_modal(self, request, web_driver):
        driver = request.getfixturevalue(web_driver)
        feed_page = FeedPage(driver)
        feed_page.get_url(FEED_PAGE)
        feed_page.click_on_first_order()
        assert feed_page.is_order_details_modal_opened()

    @allure.title('Заказы отображаются в списке заказов')
    @pytest.mark.parametrize(
        "web_driver",
        ['driver_chrome', 'driver_firefox']
    )
    def test_click_order_open_modal(self, request, web_driver, register_new_user):
        driver = request.getfixturevalue(web_driver)
        login_page = LoginPage(driver)
        login_page.get_url(LOGIN)
        login_page.click_login_with_credentials(register_new_user['email'], register_new_user['password'])

        home_page = HomePage(driver)
        home_page.drag_and_drop_first_ingredien_to_constructor()
        home_page.click_make_order_button()
        
        account_page = AccountPage(driver)
        account_page.get_url(ACCOUNT)
        account_page.click_orders_history()
        order_number = account_page.get_first_order_number()

        feed_page = FeedPage(driver)
        feed_page.get_url(FEED_PAGE)
        orders_feed = feed_page.get_list_order_numbers()
        assert order_number in orders_feed

    @allure.title('Счетчик общего числа заказов увеличивается при создании заказа')
    @pytest.mark.parametrize(
        "web_driver",
        ['driver_chrome', 'driver_firefox']
    )
    def test_overall_orders_count(self, request, web_driver, register_new_user):
        driver = request.getfixturevalue(web_driver)
        feed_page = FeedPage(driver)
        feed_page.get_url(FEED_PAGE)
        number_before = feed_page.get_overall_orders_number()

        login_page = LoginPage(driver)
        login_page.get_url(LOGIN)
        login_page.click_login_with_credentials(register_new_user['email'], register_new_user['password'])

        home_page = HomePage(driver)
        home_page.drag_and_drop_first_ingredien_to_constructor()
        home_page.click_make_order_button()

        feed_page.get_url(FEED_PAGE)
        assert feed_page.is_overall_order_counter_increased(number_before)

    @allure.title('Счетчик общего числа заказов увеличивается при создании заказа')
    @pytest.mark.parametrize(
        "web_driver",
        ['driver_chrome', 'driver_firefox']
    )
    def test_today_orders_count(self, request, web_driver, register_new_user):
        driver = request.getfixturevalue(web_driver)
        feed_page = FeedPage(driver)
        feed_page.get_url(FEED_PAGE)
        number_before = feed_page.get_todays_orders_number()

        login_page = LoginPage(driver)
        login_page.get_url(LOGIN)
        login_page.click_login_with_credentials(register_new_user['email'], register_new_user['password'])

        home_page = HomePage(driver)
        home_page.drag_and_drop_first_ingredien_to_constructor()
        home_page.click_make_order_button()

        feed_page.get_url(FEED_PAGE)
        assert feed_page.is_todays_order_counter_increased(number_before)

    @allure.title('При создании заказа, его номер отображается в списке заказов В работе')
    @pytest.mark.parametrize(
        "web_driver",
        ['driver_chrome', 'driver_firefox']
    )
    def test_order_in_progress(self, request, web_driver, register_new_user):
        driver = request.getfixturevalue(web_driver)
        login_page = LoginPage(driver)
        login_page.get_url(LOGIN)
        login_page.click_login_with_credentials(register_new_user['email'], register_new_user['password'])

        home_page = HomePage(driver)
        home_page.drag_and_drop_first_ingredien_to_constructor()
        home_page.click_make_order_button()
        time.sleep(5)
        order_id = home_page.get_order_id

        feed_page = FeedPage(driver)
        feed_page.get_url(FEED_PAGE)
        assert feed_page.is_order_in_progress(order_id)