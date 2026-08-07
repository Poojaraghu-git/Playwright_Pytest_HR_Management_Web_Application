import logging

from locators.myinfo_locator import MyInfoLocator
from pages.base_page import BasePage

logger = logging.getLogger(__name__)
class MyInfoPage(BasePage):

    def open_MyInfo_page(self):
        logger.info("Navigating to MyInfo Page")
        self.click(MyInfoLocator.MyInfo_Menu)

    def check_submenus_are_visible(self):
        logger.info("Verifying submenus are visible")
        for name, locator in MyInfoLocator.SubMenus.items():
            logger.info(f"Verifying visibility of {name} submenu")
            if not self.is_visible(locator):
                logger.info(f"{name} submenu is not visible")
                return False
            logger.info(f"{name} submenu is visible")
        return True

    def check_submenus_are_clickable(self):
        logger.info("Verifying submenus are clickable")
        for name, locator in MyInfoLocator.SubMenus.items():
            logger.info(f"{name} submenu is clickable")
            self.click(locator)
        return True