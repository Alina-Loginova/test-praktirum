import pytest
import requests
from selenium import webdriver

from helpers import generate_random_string
from pages.base_page import BasePage
from urls import REGISTER

@pytest.fixture(scope='function')
def driver_chrome():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def driver_firefox():
    driver = webdriver.Firefox()
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()

@pytest.fixture 
def register_new_user():
    login_pass = []
    email = generate_random_string(10) + '@gmail.com'
    password = generate_random_string(10)
    name = generate_random_string(10)
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    response = requests.post(REGISTER, data=payload)
    if response.status_code == 200:
        login_pass = {
        "email": email,
        "password": password,
        "name": name
    }
    return login_pass
