import logging

from locators.admin_locator import AdminLocator
from locators.homepage_locator import HomepageLocator
from pages.base_page import BasePage

logger = logging.getLogger(__name__)
class AdminPage(BasePage):
    def create_user(self):
        logger.info(f"Creating user")
        self.page.wait_for_selector(AdminLocator.Add_button, timeout=5000)
        self.page.click(AdminLocator.Add_button)
        self.page.click(AdminLocator.user_role_input)
        self.page.get_by_role("option", name="Admin").click()
        logger.info(f"Admin role clicked")
        self.page.locator(AdminLocator.employee_name_input).fill("Ran")
        self.page.get_by_role("option", name="Ranga Akunuri").click()
        logger.info(f"Ranga Akunuri clicked")
        self.page.click(AdminLocator.status_input)
        self.page.get_by_role("option", name="Enabled").click()
        logger.info(f"Enabled status clicked")
        self.page.click(AdminLocator.username_input)
        # new_username = "Ranga Ranga"
        self.page.locator(AdminLocator.username_input).fill(AdminLocator.new_username)
        logger.info(f"Username Entered")
        self.page.click(AdminLocator.password_input)
        # new_password = "Day@1234"
        self.page.locator(AdminLocator.password_input).fill(AdminLocator.new_password)
        logger.info(f"Password Entered")
        self.page.click(AdminLocator.confirm_password_input)
        self.page.locator(AdminLocator.confirm_password_input).fill(AdminLocator.new_password)
        logger.info(f"Confirm Password Entered")
        self.page.click(AdminLocator.save_button)
        logger.info(f"Clicked on Save button")
        self.page.wait_for_selector("//h5[text()='System Users']", timeout=10000)

    def search_user(self):
        self.page.click(AdminLocator.user_management_section)
        logger.info(f"Searching for user: {AdminLocator.new_username}")
        self.page.wait_for_selector(AdminLocator.username_input, timeout=5000)
        self.page.locator(AdminLocator.username_input).fill(AdminLocator.new_username)
        self.page.click(AdminLocator.save_button)
        logger.info(f"Clicked on Search button")
        self.page.wait_for_selector(AdminLocator.user_table, timeout=10000)

    def is_user_present_in_table(self):
        logger.info(f"Checking if user is present in table: {AdminLocator.new_username}")
        self.page.wait_for_selector(AdminLocator.user_table_username_cell, timeout=5000)
        rows = self.page.locator(AdminLocator.user_table_username_cell)
        count = rows.count()

        for i in range(count):
            cell_text = rows.nth(i).inner_text().strip()
            logger.info(f"Row {i+1} username: {cell_text}")
            if cell_text.lower() == AdminLocator.new_username.lower():
                logger.info(f"User {AdminLocator.new_username} found in table")
                return True
        logger.info(f"User {AdminLocator.new_username} not found in table")
        return False







