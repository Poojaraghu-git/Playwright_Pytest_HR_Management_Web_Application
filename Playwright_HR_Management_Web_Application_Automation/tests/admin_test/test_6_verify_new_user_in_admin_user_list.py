import pytest

from pages.admin_page import AdminPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utilities.excel_helper import ExcelHelper

file_path = "C:\\Users\\pooja\\PycharmProjects\\Playwright_HR_Management_Web_Application_Automation\\test_data\\test_login_details.xlsx"
sheet_name = "valid_login"
login_data = ExcelHelper.read_excel_sheet(file_path, sheet_name)

@pytest.mark.parametrize('data', login_data)
def test_verify_newly_created_user_in_admin_user_list(page, data):
    hp = HomePage(page)
    lp = LoginPage(page)
    lp.open_url()
    lp.login(data["Username"], data["Password"])
    assert hp.is_dashboard_visible(), "Dashboard is not visible"
    hp.click_admin_menu()
    ap = AdminPage(page)
    ap.search_user()
    assert ap.is_user_present_in_table(), "User is not present in table"

