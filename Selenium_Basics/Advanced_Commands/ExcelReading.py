import xlrd
import xlwt
wb=xlrd.open_workbook("C:/Users/Rohsmiles/Desktop/Book4.xlsx")
sheet=wb.sheet_by_name("Sheet1")
s=sheet.cell_value(1,2)
print(int(s))
from xlrd.book import colname
print(colname(0,"Username"))
for i in range(sheet.ncols):
    if sheet.cell_value(0,i) in "Username":
        print(sheet.cell_value(0,i))
    elif sheet.cell_value(0,i) in "UserId":
        print(int(sheet.cell_value(1,0)))
