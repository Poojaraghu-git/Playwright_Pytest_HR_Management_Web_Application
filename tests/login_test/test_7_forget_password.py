import logging

from locators.login_locator import LoginLocators
from pages.login_page import LoginPage

logger = logging.getLogger(__name__)
def test_forget_password_functionality(page):
    lp = LoginPage(page)
    # lp.open_url()
    lp.forgot_password()
    reset_password_message = lp.page.locator(LoginLocators.reset_password_success_message).inner_text()
    logger.info(f"{reset_password_message} is displayed")
    assert "success" in reset_password_message

