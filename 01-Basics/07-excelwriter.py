
import xlsxwriter

workbook = xlsxwriter.Workbook('07-data.xlsx')
worksheet = workbook.add_worksheet()

d = { 'a': ['e1', 'e2', 'e3'], 'b': ['e1', 'e2'], 'c': ['e1']}

row = 0
col = 0

for key in d.keys():
    row += 1
    worksheet.write(row, col, key)
    for item in d[key]:
        worksheet.write(row, col + 1, item)
        row += 1

workbook.close()