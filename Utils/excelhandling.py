def test_excelhandling():
    import openpyxl
    workbook = openpyxl.load_workbook("testData/creds.xlsx")
    sheet = workbook.active
    values=[]
   # print(sheet.cell(row=1, column=1).value)
    for i in sheet.iter_rows(values_only=True):