#!usr/bin/env python3
import sys
from xlrd import open_workbook

input_file = sys.argv[1]

workbook = open_workbook(input_file)
print('Number of worksheet : ', workbook.nsheets)
for worksheet in workbook.sheets():
    print("Worksheet name: ", worksheet.name, "\tRows: " , worksheet.nrows, "\tcolumns:", worksheet.ncols)

