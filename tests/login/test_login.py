import pytest
from framework.login_consts import LoginConsts
import logging

logger = logging.getLogger(__name__)


@pytest.mark.parametrize('email, password, expectation',
                         [('qa.ajax.app.automation@gmail.com', 'qa_automation_password', True),
                          ('lol@mail.lol', 'lol', False),
                          (' ', ' ', False),
                          ])
def test_user_login(email, password, expectation, user_login_fixture):
    logging.info("Set implicitly wait for 5 seconds")
    user_login_fixture.implicitly_wait(5)
    logger.info("Precondition - Log In button is displayed")
    assert user_login_fixture.is_element_on_page(LoginConsts.FIRST_LOGIN_BUTTON), \
        f"Can't verify that Log In button is on page"
    # region - test steps
    logger.info("Step 1 - Log In page is displayed")
    user_login_fixture.click_first_login()
    logger.info("Step 2 - Second Log In button is displayed ")
    assert user_login_fixture.is_element_on_page(LoginConsts.EMAIL_INPUT)
    logger.info("Step 3 - Email value was set")
    user_login_fixture.set_email(email)
    logger.info("Step 4 - Email value was successfully verified")
    assert user_login_fixture.verify_email_value(email)
    logger.info("Step 5 - Password value was set to password-field")
    user_login_fixture.set_password(password)
    logger.info("Step 6 - Password value was successfully verified")
    assert user_login_fixture.verify_password_value(password)
    logger.info("Step 7 - Log In button was pressed")
    user_login_fixture.click_second_login()
    if expectation:
        logger.info("Step 8 - Main page is displayed")
    else:
        logger.info("Step 8 - Main page isn't displayed")
    assert user_login_fixture.is_element_on_page(LoginConsts.SIDEBAR_BUTTON) == expectation
    # endregion
