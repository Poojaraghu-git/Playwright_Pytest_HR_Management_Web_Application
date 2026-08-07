import logging

from locators.admin_locator import AdminLocator
from locators.homepage_locator import HomepageLocator
from locators.login_locator import LoginLocators
from pages.base_page import BasePage

logger = logging.getLogger(__name__)
class HomePage(BasePage):

    def is_dashboard_visible(self):
        self.page.wait_for_selector(HomepageLocator.Dashboard_locator, timeout=5000)
        return self.is_visible(HomepageLocator.Dashboard_locator)

    def click_admin_menu(self):
        logger.info(f"Clicking Admin menu")
        return self.page.click(HomepageLocator.Admin_Menu_locator)

    def click_logout(self):
        self.page.wait_for_selector(HomepageLocator.Profile_Menu, timeout=5000)
        self.page.click(HomepageLocator.Profile_Menu)
        logger.info(f"Clicked Profile Menu")
        self.page.click(HomepageLocator.Logout_Button)
        logger.info(f"Clicked Logout button")








