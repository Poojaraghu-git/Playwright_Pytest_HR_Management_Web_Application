import logging

from locators.homepage_locator import HomepageLocator
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class MenuPage(BasePage):

    def verify_menu_items_are_visible(self):
        for name,locator in HomepageLocator.Items.items():
            logger.info(f"Verifying visibility of {name} Menu")
            if not self.is_visible(locator):
                logger.info(f"{name} Menu is not visible")
                return False
            logger.info(f"{name} Menu is visible")
        return True

    def verify_menu_items_are_clickable(self):
        for name,locator in HomepageLocator.Items.items():
            logger.info(f"Verifying clickability of {name} Menu")
            logger.info(f"Clicking on {name} Menu")
            self.click(locator)
        return True

