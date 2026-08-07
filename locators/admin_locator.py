

class AdminLocator:
    Add_button = "//button[@type='button' and @class='oxd-button oxd-button--medium oxd-button--secondary']"
    user_role_input = "//label[text()='User Role']/../following-sibling::div//div[contains(@class,'oxd-select-text-input')]"
    employee_name_input = "//input[@placeholder='Type for hints...']"
    status_input = "//label[text()='Status']/../following-sibling::div//div[contains(@class,'oxd-select-text-input')]"
    username_input = "//label[text()='Username']/../following-sibling::div/input"
    password_input = "//label[text()='Password']/../following-sibling::div//input[@type='password']"
    confirm_password_input = "//label[text()='Confirm Password']/../following-sibling::div//input[@type='password']"
    save_button = "//button[@type='submit']"
    user_management_section = "//span[text()='User Management ']"
    user_table = "//div[@class='oxd-table-card']"
    user_table_username_cell = "//div[@class='oxd-table-body']//div[@role='row']//div[2]"
    new_username = "Ranga Rathy"
    new_password = "Day@1234"
