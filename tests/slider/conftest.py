import pytest

from framework.sidebar_page import SliderPage
from framework.login_page import LoginPage


@pytest.fixture(scope='function', autouse=True)
def user_login_fixture(driver):
    driver.launch_app()
    yield LoginPage(driver)
    driver.close_app()


@pytest.fixture(scope='function', autouse=True)
def sidebar_fixture(driver):
    driver.launch_app()
    yield SliderPage(driver)
    driver.close_app()
