import logging

from locators.admin_locator import AdminLocator
from locators.login_locator import LoginLocators
from pages.base_page import BasePage

logger = logging.getLogger(__name__)
class LoginPage(BasePage):


    def open_url(self):
        self.goto("https://opensource-demo.orangehrmlive.com")

    def login(self, username: str, password: str):
        self.fill(LoginLocators.Username_Input, username)
        logger.info(f"Logging in with username: {username}")
        self.fill(LoginLocators.Password_Input, password)
        logger.info(f"Logging in with password: {password}")
        self.click(LoginLocators.Submit_button)
        logger.info("Clicked on the submit button")


    def is_login_page_loaded(self):
        return self.is_visible(LoginLocators.Username_Input) and self.is_visible(LoginLocators.Password_Input)

    def is_username_visible(self):
        logger.info(f"Checking visibility of username input: {LoginLocators.Username_Input}")
        return self.is_visible(LoginLocators.Username_Input)

    def is_password_visible(self):
        logger.info(f"Checking visibility of password input: {LoginLocators.Password_Input}")
        return self.is_visible(LoginLocators.Password_Input)

    def enter_new_login_details(self):
        logger.info(f"Entering username")
        self.page.locator(LoginLocators.Username_Input).fill(AdminLocator.new_username)
        logger.info(f"Entering password")
        self.page.locator(LoginLocators.Password_Input).fill(AdminLocator.new_password)
        self.page.click(LoginLocators.Submit_button)
        logger.info(f"Clicked Submit button")

    def forgot_password(self):
        self.page.click(LoginLocators.forget_password)
        logger.info("Clicked on Forgot Password link")
        self.page.wait_for_selector(LoginLocators.reset_password_text, timeout=5000)
        reset_password = self.page.locator(LoginLocators.reset_password_text).inner_text()
        logger.info(f"{reset_password} text is present")
        self.page.click(LoginLocators.reset_username)
        self.page.locator(LoginLocators.reset_username).fill(AdminLocator.new_username)
        self.page.click(LoginLocators.reset_submit_button)
        logger.info(f"Clicked Submit button")


