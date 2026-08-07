import logging

from playwright.sync_api import Page , TimeoutError as PlaywrightTimeoutError

from utilities.screenshot_helper import ScreenshotHelper

logger = logging.getLogger(__name__)

class BasePage:

    def __init__(self, page:Page):
        self.page = page
        self.screenshot = ScreenshotHelper(page)

    def goto(self, url:str):
        logger.info(f"Navigating to {url}")
        self.page.goto(url)

    def wait_for_visible(self, locator:str, timeout:int=3000):
        try:
            self.page.wait_for_selector(locator, state="visible", timeout=timeout)
            logger.info(f"Element is visible: {locator}")
        except PlaywrightTimeoutError:
            logger.error(f"Element is not visible: {locator}")
            raise

    def click(self, locator:str):
        logger.info(f"Clicking the {locator}")
        self.page.click(locator)

    def fill(self, locator:str, text:str):
        # logger.info(f"Filling the {locator} with {text} ")
        self.wait_for_visible(locator)
        self.page.fill(locator, text)

    def is_visible(self, locator:str) -> bool:
        try:
            self.page.wait_for_selector(locator, state="visible", timeout=3000)
            logger.info(f"Element is visible: {locator}")
            return True
        except PlaywrightTimeoutError:
            logger.error(f"Element is not visible: {locator}")
            return False



