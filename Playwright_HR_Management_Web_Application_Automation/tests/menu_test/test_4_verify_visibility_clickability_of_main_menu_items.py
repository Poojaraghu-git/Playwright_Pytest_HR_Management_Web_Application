import pytest

from pages import login_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from utilities.excel_helper import ExcelHelper

file_path = "C:\\Users\\pooja\\PycharmProjects\\Playwright_HR_Management_Web_Application_Automation\\test_data\\test_login_details.xlsx"
sheet_name = "valid_login"
login_data = ExcelHelper.read_excel_sheet(file_path, sheet_name)

@pytest.mark.parametrize('data', login_data)
def test_main_menu_items_visibility_and_clickability(page,data):
    lp = LoginPage(page)
    # lp.open_url()
    hp = HomePage(page)
    lp.login(data["Username"], data["Password"])
    assert hp.is_dashboard_visible(), "Dashboard is not visible"
    mp = MenuPage(page)
    assert mp.verify_menu_items_are_visible(), "One or more menu items are not visible"
    assert mp.verify_menu_items_are_clickable(), "One or more menu items are not clickable"