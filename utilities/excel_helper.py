import openpyxl
from openpyxl.styles import PatternFill


class ExcelHelper:
    @staticmethod
    def read_excel_sheet(file_path: str, sheet_name: str):

        wb = openpyxl.load_workbook(file_path, data_only=True)
        sheet = wb[sheet_name]

        # data_list =[]
        headers = [str(cell.value).strip() for cell in sheet[1]]
        print("headers: ", headers)

        data_list = []
        for row in sheet.iter_rows(min_row=2, values_only=True):
            row_dict =dict(zip(headers,row))
            data_list.append(row_dict)
        wb.close()
        return data_list

    @staticmethod
    def write_excel_sheet(file_path: str, sheet_name: str, test_id: str, test_result: str):
        wb = openpyxl.load_workbook(file_path)
        sheet = wb[sheet_name]

        headers = [cell.value for cell in sheet[1]]
        if "Test Result" not in headers:
            sheet.cell(row=1, column=len(headers)+1).value="Test Result"
            result_col = len(headers)+1
        else:
            result_col = headers.index("Test Result")+ 1

        test_id_col = headers.index("Test ID")+1

        # Find the row for the given test_id
        for row in range(2, sheet.max_row+1):
            if sheet.cell(row=row, column=test_id_col).value == test_id:
                sheet.cell(row=row, column=result_col).value = test_result
                if test_result.lower() == "pass":
                    sheet.cell(row=row, column=result_col).fill = PatternFill(fill_type="solid", start_color="00FF00")
                else:
                    sheet.cell(row=row, column=result_col).fill = PatternFill(fill_type="solid", start_color="FF0000")
                break
        wb.save(file_path)
        wb.close()