from framework.sidebar_consts import SideBarConsts
from framework.login_page import LoginConsts
import logging

logger = logging.getLogger(__name__)


def test_sidebar(sidebar_fixture, user_login_fixture):
    user_login_fixture.login_to_application('qa.ajax.app.automation@gmail.com', 'qa_automation_password')
    sidebar_fixture.implicitly_wait(5)
    logger.info("Precondition - SideBar button is displayed")
    assert user_login_fixture.is_element_on_page(SideBarConsts.SIDEBAR_BUTTON)
    # region - test steps
    logger.info("Step 1 - SideBar is opened")
    sidebar_fixture.click_on_sidebar()
    logger.info("Step 2 - 'Add hub' button has text 'Add hub'")
    assert sidebar_fixture.verify_element_and_text(SideBarConsts.ADD_HUB_LABEL, "Add hub")
    logger.info("Step 3 - 'App Settings' button has text 'App Settings'")
    assert sidebar_fixture.verify_element_and_text(SideBarConsts.APP_SETTINGS_LABEL, "App Settings")
    logger.info("Step 4 - 'Help' button has text 'Help'")
    assert sidebar_fixture.verify_element_and_text(SideBarConsts.HELP_LABEL, "Help")
    logger.info("Step 5 - 'Report a problem' button has text 'Report a problem'")
    assert sidebar_fixture.verify_element_and_text(SideBarConsts.REPORT_A_PROBLEM_LABEL, "Report a problem")
    # endregion
