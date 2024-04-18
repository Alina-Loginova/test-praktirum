import allure
import pytest

from pages.feed_page import FeedPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from urls import HOME, LOGIN


@allure.story('Основной функционал')
class TestMainPage:

    @allure.title('Переход в конструктор')
    @pytest.mark.parametrize(
        "web_driver",
        ['driver_chrome', 'driver_firefox']
    )
    def test_go_to_constructor(self, request, web_driver):
        driver = request.getfixturevalue(web_driver)
        home_page = HomePage(driver)
        home_page.get_url(HOME)
        home_page.click_on_constructor()
        assert home_page.ingredients_block_is_visible()


    @allure.title('Переход в ленту заказов')
    @pytest.mark.parametrize(
        "web_driver",
        ['driver_chrome', 'driver_firefox']
    )
    def test_go_to_feed_orders(self, request, web_driver):
        driver = request.getfixturevalue(web_driver)
        home_page = HomePage(driver)
        home_page.get_url(HOME)
        home_page.click_on_orders_feed()

        feed_page = FeedPage(driver)
        assert feed_page.is_orders_feed_list_visible()

    @allure.title('Переход в ленту заказов')
    @pytest.mark.parametrize(
        "web_driver",
        ['driver_chrome', 'driver_firefox']
    )
    def test_open_ingredient_list(self, request, web_driver):
        driver = request.getfixturevalue(web_driver)
        home_page = HomePage(driver)
        home_page.get_url(HOME)
        home_page.click_on_first_ingredient()
        assert home_page.modal_ingredient_window_is_opened()

    @allure.title('Нажатие на крестик на модалке ингредиента')
    @pytest.mark.parametrize(
        "web_driver",
        ['driver_chrome', 'driver_firefox']
    )
    def test_close_ingredient_list(self, request, web_driver):
        driver = request.getfixturevalue(web_driver)
        home_page = HomePage(driver)
        home_page.get_url(HOME)
        home_page.click_on_first_ingredient()
        home_page.click_on_close_button()
        assert not home_page.modal_ingredient_window_is_opened()

    @allure.title('Счетчик ингредиента увеличивается после его добавления в конструктор')
    @pytest.mark.parametrize(
        "web_driver",
        ['driver_chrome', 'driver_firefox']
    )
    def test_count_after_ingredient_add(self, request, web_driver):
        driver = request.getfixturevalue(web_driver)
        home_page = HomePage(driver)
        home_page.get_url(HOME)
        home_page.drag_and_drop_first_ingredien_to_constructor()
        assert home_page.get_ingredient_count() == 2

    @allure.title('Авторизованный пользователь имеет возможность создать заказ')
    @pytest.mark.parametrize(
        "web_driver",
        ['driver_chrome', 'driver_firefox']
    )
    def test_auth_create_order(self, request, web_driver, register_new_user):
        driver = request.getfixturevalue(web_driver)
        login_page = LoginPage(driver)
        login_page.get_url(LOGIN)
        login_page.click_login_with_credentials(register_new_user['email'], register_new_user['password'])

        home_page = HomePage(driver)
        home_page.drag_and_drop_first_ingredien_to_constructor()
        home_page.click_make_order_button()
        assert home_page.is_modal_order_number_present()