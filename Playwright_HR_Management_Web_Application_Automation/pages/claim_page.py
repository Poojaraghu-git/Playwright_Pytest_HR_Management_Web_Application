import logging

from locators.claim_locator import ClaimLocator
from pages.base_page import BasePage


logger = logging.getLogger(__name__)
class ClaimPage(BasePage):

    def open_claim_section(self):
        logger.info("Navigating to Claim section")
        self.page.click(ClaimLocator.Claim_Menu)
        self.page.click(ClaimLocator.Submit_Claim_Section)

    def submit_claim(self, claim_type, currency, reason):
        logger.info("Submitting new claim")

        self.page.click(ClaimLocator.Claim_Type_Input)
        self.page.click(f"//span[text()='{claim_type}']")
        logger.info(f"Selected claim type: {claim_type}")

        self.page.click(ClaimLocator.Currency_Input)
        self.page.click(f"//span[text()='{currency}']")
        logger.info(f"Selected currency: {currency}")

        self.page.locator("//textarea").fill(reason)
        logger.info(f"Entered reason: {reason}")

        self.page.click(ClaimLocator.Claim_Submit_Button)
        logger.info("Clicked Submit button")

        self.page.wait_for_timeout(5000)

        self.page.wait_for_selector(ClaimLocator.Submit_Claim_Menu, timeout=5000)

    def add_expense(self, expense_type, date, amount, notes):
        logger.info("Adding expense")

        self.page.click(ClaimLocator.Add_Expense_Button)

        self.page.click(ClaimLocator.Expense_Type_Input)
        self.page.click(f"//span[text()='{expense_type}']")

        self.page.fill(ClaimLocator.Date_Input, date)

        self.page.locator(ClaimLocator.Amount_Input).fill(str(amount))

        self.page.click(ClaimLocator.Save_Expense_Button)
        logger.info("Expense saved")

        self.page.wait_for_selector(ClaimLocator.New_Record_Table, timeout=8000)

    def submit_claim_successfully(self):
        logger.info("Submitting claim")

        self.page.click(ClaimLocator.Final_Submit_Button)
        logger.info("Clicked Submit button")

    def verify_claim_success(self):
        logger.info("Checking for successful claim submission")
        try:
            self.page.wait_for_url("**/claim/submitClaim/id/**", timeout=8000)
            logger.info("Claim submission successful")
            return True
        except Exception as e:
            logger.error(f"Success submission failed. Error: {e}")
            self.screenshot.take_screenshot("claim_submission_failed")
            return False

    def verify_claim_in_history(self, claim_type, amount):
        logger.info("Checking claim in history")

        self.page.click(ClaimLocator.My_Claim_Section)
        self.page.wait_for_selector(ClaimLocator.My_Claim_Records, timeout=5000)

        rows = self.page.locator(ClaimLocator.My_Claim_Records)
        count = rows.count()

        for i in range(count):
            row_text = rows.nth(i).inner_text().strip()
            logger.info(f"Row {i + 1}: {row_text}")
            import re
            match = re.search(r"([\d,]+\.\d{2})",row_text)
            if match:
                table_amount = float(match.group(1).replace(",", ""))

                if claim_type in row_text and table_amount == float(amount):
                    logger.info("Claim found in history")
                    return True

        self.screenshot.take_screenshot("claim_not_found_in_history")
        logger.error("Claim not found in history")
        return False

