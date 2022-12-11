import pytest
from framework.sidebar_consts import SideBarConsts
from framework.login_page import LoginConsts
import time
import logging

logger = logging.getLogger(__name__)


def test_sidebar(sidebar_fixture, user_login_fixture):
    user_login_fixture.login_to_application('qa.ajax.app.automation@gmail.com', 'qa_automation_password')
    sidebar_fixture.implicitly_wait(5)
    logger.info("Precondition - verify that SideBar is on page")
    assert user_login_fixture.is_element_on_page(LoginConsts.SIDEBAR)
    logger.info("Step 1 - Click on SideBar button")
    sidebar_fixture.click_on_sidebar()
    logger.info("Step 2 - Verify 'Add hub' element")
    assert sidebar_fixture.verify_element_and_text(SideBarConsts.ADD_HUB_LABEL, "Add hub")
    logger.info("Step 2 - Verify 'App Settings' element")
    assert sidebar_fixture.verify_element_and_text(SideBarConsts.APP_SETTINGS_LABEL, "App Settings")
    logger.info("Step 2 - Verify 'Help' element")
    assert sidebar_fixture.verify_element_and_text(SideBarConsts.HELP_LABEL, "Help")
    logger.info("Step 2 - Verify 'Report a problem' element")
    assert sidebar_fixture.verify_element_and_text(SideBarConsts.REPORT_A_PROBLEM_LABEL, "Report a problem")


