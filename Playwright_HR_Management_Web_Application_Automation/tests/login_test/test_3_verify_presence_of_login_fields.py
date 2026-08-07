import logging
from logging import Logger

import pytest

from pages.login_page import LoginPage
from utilities.excel_helper import ExcelHelper

file_path = "C:\\Users\\pooja\\PycharmProjects\\Playwright_HR_Management_Web_Application_Automation\\test_data\\test_login_details.xlsx"
sheet_name = "valid_login"
login_data = ExcelHelper.read_excel_sheet(file_path, sheet_name)

logger = logging.getLogger(__name__)

@pytest.mark.parametrize("data", login_data)
def test_login_fields_are_visible(page, data):
    lp = LoginPage(page)
    # lp.open_url()
    assert lp.is_username_visible()
    logger.info(f"Username is visible")
    assert lp.is_password_visible()
    logger.info(f"Password is visible")
    lp.login(data['Username'],data['Password'])
    logger.info(f"Username - {data['Username']} and Password - {data['Password']} is enabled and entered")