from selenium.webdriver.common.by import By


class HomePageLocators:

    ACCOUNT = By.XPATH, '//*[contains(text(),"Личный Кабинет")]'
    CONSTRUCTOR = By.XPATH, '//li/a[@href="/"]'
    INGREDIENTS_BLOCK = By.CSS_SELECTOR, '[class*="BurgerIngredients_ingredients__menuContainer"]'
    ORDERS_FEED = By.CSS_SELECTOR, '[href="/feed"]'
    INGREDIENTS_LIST_ELEMENTS = By.CSS_SELECTOR, '[href*="/ingredient"]'
    MODAL_INGREDIENT_OPENED = By.CSS_SELECTOR, '[class*="Modal_modal_opened"]'
    BURGER_CONSTRUCTOR = By.CSS_SELECTOR, 'ul[class*="BurgerConstructor_basket__list"]'
    COUNTERS_ELEMENTS = By.CSS_SELECTOR, 'p[class*="counter_counter__num"]'
    CLOSE_MODAL = By.CSS_SELECTOR, '[class*="Modal_modal__close"]'
    MAKE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'
    MODAL_ORDER_NUMBER = By.CSS_SELECTOR, '[class*="Modal_modal__contentBox"]'
    ORDER_ID = By.XPATH, '//*[@id="root"]/div/section/div[1]/div/h2'
