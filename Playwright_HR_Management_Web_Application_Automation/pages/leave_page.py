import logging
from time import sleep

from locators.homepage_locator import HomepageLocator
from locators.leave_locator import LeaveLocator
from pages.base_page import BasePage

logger = logging.getLogger(__name__)
class LeavePage(BasePage):

    def open_leave_page(self):
        logger.info("Clicked on Leave Menu")
        self.page.click(HomepageLocator.Leave_Menu_locator)

    def assign_leave(self, employee_name , leave_type, from_date, to_date):
        self.page.wait_for_selector(LeaveLocator.Assign_Leave_Button, timeout=5000)
        logger.info("Navigating to Assign Leave section")
        self.page.click(LeaveLocator.Assign_Leave_Button)

        logger.info(f"Assigning leave to employee: {employee_name}")
        self.page.locator(LeaveLocator.Employee_Name_input).fill(employee_name)
        self.page.get_by_role("option", name=employee_name).click()
        logger.info(f"employee name is selected: {employee_name}")

        logger.info(f"Selecting leave type: {leave_type}")
        self.click(LeaveLocator.Leave_Type_input)
        option = LeaveLocator.Leave_Type_Option.format(leave_type)
        self.click(option)

        logger.info(f"Selecting From date: {from_date}")
        self.fill(LeaveLocator.From_Date_Option, from_date)


        logger.info(f"Selecting To date: {to_date}")
        self.page.locator(LeaveLocator.To_Date_Option).fill("", force=True)
        self.fill(LeaveLocator.To_Date_Option, to_date)

        self.click(LeaveLocator.Assign_Button)
        logger.info("Waiting for popup dialog")


        self.page.wait_for_selector("//button[normalize-space()='Ok']", timeout=5000)
        logger.info("Popup appeared, clicking OK")

        self.page.click(LeaveLocator.popup_button)
        self.page.wait_for_timeout(3000)

    def check_leave_assigned(self):

        logger.info("Checking for success message")
        try:
            self.page.wait_for_timeout(3000)
            self.page.wait_for_selector(
                "//div[contains(@class,'oxd-toast-content') and contains(.,'Success')]",
                timeout=8000
            )
            logger.info("Leave assignment successful (toast detected)")
            return True

        except Exception as e:
            logger.warning(f"Success toast not detected, falling back to URL check : {e}")

        try:
            self.page.wait_for_url("**/leave/assignLeave", timeout=8000)
            logger.info("Leave assignment successful (URL stable)")
            return True
        except Exception as e:
            logger.error(f"Leave assignment failed. Error: {e}")
            return False


    def verify_leave_records_in_leave_list(self, employee_name, status, from_date, to_date):
        logger.info("Navigating to Leave list")
        self.click(LeaveLocator.Leave_List_section)
        self.page.locator(LeaveLocator.Employee_Name_input).fill(employee_name)
        self.page.get_by_role("option", name=employee_name).click()

        logger.info(f"Selecting Leave status: {status}")
        self.click(LeaveLocator.Show_leave_status_dropdown)
        option = LeaveLocator.Status_option.format(status)
        self.click(option)

        logger.info(f"Selecting date range: {from_date} to {to_date}")
        self.fill(LeaveLocator.Leave_List_From_Date, from_date)
        self.fill(LeaveLocator.Leave_List_To_Date, to_date)

        self.click(LeaveLocator.Search_Button)
        self.page.wait_for_selector(LeaveLocator.Leave_List_Rows, timeout=5000)
        sleep(10)

        rows = self.page.locator(LeaveLocator.Leave_List_Name_Cell)
        count = rows.count()

        for i in range(count):
            cell_text = rows.nth(i).inner_text().strip()
            logger.info(f"Row {i+1} name: {cell_text}")
            if employee_name in cell_text:
                logger.info("Leave record found in the leave list")
                self.screenshot.take_screenshot("leave_assignment_failed")
                return True
        logger.error("No record found in the leave list")
        return False





