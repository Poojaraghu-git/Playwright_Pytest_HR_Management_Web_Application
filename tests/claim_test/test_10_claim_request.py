import pytest

from pages.claim_page import ClaimPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utilities.excel_helper import ExcelHelper

file_path = "C:\\Users\\pooja\\PycharmProjects\\Playwright_HR_Management_Web_Application_Automation\\test_data\\test_login_details.xlsx"
sheet_name = "valid_login"
login_data = ExcelHelper.read_excel_sheet(file_path, sheet_name)

@pytest.mark.parametrize('data', login_data)
def test_initiate_claim_request(page, data):
    hp = HomePage(page)
    lp = LoginPage(page)
    # lp.open_url()
    lp.login(data["Username"], data["Password"])
    assert hp.is_dashboard_visible(), "Dashboard is not visible"

    cp = ClaimPage(page)
    cp.open_claim_section()
    cp.submit_claim("Travel Allowance", "Indian Rupee", "Client meeting travel reimbursement")
    cp.add_expense("Accommodation", "2026-08-04", 1500, "Taxi + food")
    cp.submit_claim_successfully()

    assert cp.verify_claim_success(), "Claim was not submitted successfully"
    assert cp.verify_claim_in_history("Travel Allowance", 1500), "Claim not found in history"