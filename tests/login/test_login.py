import pytest
from framework.login_consts import LoginConsts
import logging


logger = logging.getLogger(__name__)


@pytest.mark.parametrize('email, password, expectation',
                         [('qa.ajax.app.automation@gmail.com', "qa_automation_password", True),
                          ('lol@mail.lol', 'lol', False),
                          (' ', ' ', False),
                          ])
def test_user_login(email, password, expectation, user_login_fixture):
    logging.info("Set implicitly wait for 5 seconds")
    user_login_fixture.implicitly_wait(5)
    logger.info("Precondition - verify that Log In button is on page")
    assert user_login_fixture.is_element_on_page(LoginConsts.FIRST_LOGIN), \
        f"Can't verify that Log In button is on page"
    # region - test details
    logger.info("Step 1 - Click on Log In button")
    user_login_fixture.click_first_login()
    logger.info("Step 2 - Verify Log In button action")
    assert user_login_fixture.is_element_on_page(LoginConsts.EMAIL)
    logger.info("Step 3 - Set correct email to email-field")
    user_login_fixture.set_email(email)
    logger.info("Step 4 - Verify email value")
    assert user_login_fixture.verify_email_value(email)
    logger.info("Step 5 - Set correct password to password-field")
    user_login_fixture.set_password(password)
    logger.info("Step 6 - Verify password value")
    assert user_login_fixture.verify_password_value(password)
    logger.info("Step 7 - Click on Log In button")
    user_login_fixture.click_second_login()
    logger.info("Step 8 - Verify Log In button action")
    assert user_login_fixture.is_element_on_page(LoginConsts.SIDEBAR) == expectation

