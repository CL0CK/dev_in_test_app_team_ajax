from framework.page import Page
from framework.sidebar_consts import SideBarConsts
from tests.conftest import driver


class SliderPage(Page):

    def __init__(self, driver: driver):
        super().__init__(driver)

    def click_on_sidebar(self):
        element = self.find_element(SideBarConsts.SIDEBAR)
        self.click_element(element)
