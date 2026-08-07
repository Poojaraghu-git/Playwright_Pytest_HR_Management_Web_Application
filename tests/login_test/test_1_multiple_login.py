import logging

import pytest

from locators.login_locator import LoginLocators
from pages.home_page import HomePage
from utilities.excel_helper import ExcelHelper
from pages.login_page import LoginPage

file_path = "C:\\Users\\pooja\\PycharmProjects\\Playwright_HR_Management_Web_Application_Automation\\test_data\\test_login_details.xlsx"
sheet_name = "login_details"
login_data = ExcelHelper.read_excel_sheet(file_path, sheet_name)

logger = logging.getLogger(__name__)

@pytest.mark.parametrize("data", login_data)
def test_verify_multiple_logins(page, data):
    lp = LoginPage(page)
    lp.open_url()
    hp = HomePage(page)
    lp.login(data["Username"], data["Password"])

    expected = data["Expected Result"].lower()
    if expected == "success":
        logger.info(f"Checking Dashboard visibility for Login Successful")
        assert hp.is_dashboard_visible(), "Dashboard is not visible"
        ExcelHelper.write_excel_sheet(file_path, sheet_name, data["Test ID"], "Pass")

    else:
        logger.info("Checking error message for invalid login")
        page.wait_for_selector(LoginLocators.Error_Message, timeout=5000)
        error_msg = page.locator(LoginLocators.Error_Message)
        assert error_msg.is_visible(), "Error message is not displayed"
        error_msg_text = error_msg.inner_text().strip()
        logger.info(f"Error message: {error_msg_text}")
        assert error_msg_text.lower() == "invalid credentials", "Error message is not displayed"
        ExcelHelper.write_excel_sheet(file_path, sheet_name, data["Test ID"], "Fail")
