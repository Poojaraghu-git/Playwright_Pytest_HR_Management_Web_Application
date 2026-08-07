
class LeaveLocator:

    Assign_Leave_Button = "//a[text()='Assign Leave']"
    Employee_Name_input = "//input[@placeholder='Type for hints...']"
    Employee_Option = "//div[@role='option']"
    Leave_Type_input = "//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']"
    Leave_Type_Option = "//div[@role='option']//span[text()='CAN - Vacation']"
    From_Date_Option = "//label[text()='From Date']/../following-sibling::div//input[@placeholder='yyyy-dd-mm']"
    To_Date_Option = "//label[text()='To Date']/../following-sibling::div//input[@placeholder='yyyy-dd-mm']"
    Assign_Button = "//button[@type='submit']"
    popup_button = "//button[text()=' Ok ']"
    Success_Message = "//div[contains(text(),'Successfully Assigned')]"

    Leave_List_section = "//a[text()='Leave List']"
    Show_leave_status_dropdown = "//label[text()='Show Leave with Status']/../following-sibling::div//div[contains(@class,'oxd-select-text-input')]"
    Status_option = "//div[@role='option']//span[text()='Scheduled']"
    Leave_List_From_Date = "//label[text()='From Date']/../following-sibling::div//input[@placeholder='yyyy-dd-mm']"
    Leave_List_To_Date = "//label[text()='To Date']/../following-sibling::div//input[@placeholder='yyyy-dd-mm']"
    Search_Button = "//button[text()=' Search ']"

    Leave_List_Rows = "//div[@class='oxd-table-body']/div"
    Leave_List_Name_Cell = "//div[@class='oxd-table-body']//div[@role='row']//div[3]"
