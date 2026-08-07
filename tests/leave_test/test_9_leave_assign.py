import pytest

from pages.home_page import HomePage
from pages.leave_page import LeavePage
from pages.login_page import LoginPage
from utilities.excel_helper import ExcelHelper

file_path = "C:\\Users\\pooja\\PycharmProjects\\Playwright_HR_Management_Web_Application_Automation\\test_data\\test_login_details.xlsx"
sheet_name = "valid_login"
login_data = ExcelHelper.read_excel_sheet(file_path, sheet_name)

@pytest.mark.parametrize('data', login_data)
def test_verify_assign_leave_is_successful(page, data):
    hp = HomePage(page)
    lp = LoginPage(page)
    # lp.open_url()
    lp.login(data["Username"], data["Password"])
    assert hp.is_dashboard_visible(), "Dashboard is not visible"
    lep = LeavePage(page)
    lep.open_leave_page()

    employee_name = "Employee"
    leave_type = "CAN - Vacation"
    from_date = "2026-08-28"
    to_date = "2026-08-29"
    status = "Scheduled"
    lep.assign_leave(employee_name, leave_type, from_date, to_date)
    assert lep.check_leave_assigned(), "Leave was not assigned successfully"
    assert lep.verify_leave_records_in_leave_list(employee_name,status,from_date,to_date), "Leave not found in records in leave_list"



