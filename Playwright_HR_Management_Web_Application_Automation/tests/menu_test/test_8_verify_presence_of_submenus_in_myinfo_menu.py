import pytest

from pages import login_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from pages.myinfo_page import MyInfoPage
from utilities.excel_helper import ExcelHelper

file_path = "C:\\Users\\pooja\\PycharmProjects\\Playwright_HR_Management_Web_Application_Automation\\test_data\\test_login_details.xlsx"
sheet_name = "valid_login"
login_data = ExcelHelper.read_excel_sheet(file_path, sheet_name)

@pytest.mark.parametrize('data', login_data)
def test_verify_myinfo_submenu_items_are_visible_and_clickable(page, data):
    lp = LoginPage(page)
    # lp.open_url()
    hp = HomePage(page)
    lp.login(data["Username"], data["Password"])
    assert hp.is_dashboard_visible(), "Dashboard is not visible"
    mip = MyInfoPage(page)
    mip.open_MyInfo_page()
    assert mip.check_submenus_are_visible(), "One or more menu items are not visible"
    assert mip.check_submenus_are_clickable(), "One or more menu items are not visible"