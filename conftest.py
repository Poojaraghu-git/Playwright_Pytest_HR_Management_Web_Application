import logging

import pytest
from playwright.sync_api import sync_playwright

from utilities.logger_helper import logger


@pytest.fixture(scope="session",autouse=True)
def setup_logging():
    logger()
    logging.info("Test session started")

@pytest.fixture
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, args=['--start-maximized'])
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    page = browser.new_page(no_viewport=True)
    page.goto("https://opensource-demo.orangehrmlive.com")
    yield page
    page.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path, full_page=True)
            print(f"Screenshot saved: {screenshot_path}")

