import xlwt

wkbk=xlwt.Workbook()
sheet1=wkbk.add_sheet('Sheet1',cell_overwrite_ok=True)
sheet1.row(1).write(0,'data')
sheet1.row(0).write(0,'over ride')
wkbk.save("C:/Users/Rohsmiles/Desktop/Book5.xls")