#!user/bin/env python3

# parsing하는 방법
# 한 엑셀 파일에 여러 개의 워크시트가 포함되어 있고, 
# 그중 한 워크시트에 포함된 데이터만 필요해서 그 워크시트를 뽑아서 
# 새로운 파일로 만들어서 생성.

import sys
from xlrd import open_workbook
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()  # xlwt의 Workbook 객체를 인ㅅ턴스화하여 결과를 출력하여 엑셀에 쓸수있음.
output_worksheet = output_workbook.add_sheet('jan_2013_output')

with open_workbook(input_file) as workbook:    #xlrd의 open_workbook()함수를 사용하여 입력되는 엑셀을 workbook객체로 연다.
    worksheet = workbook.sheet_by_name('january_2013')
    for row_index in range(worksheet.nrows):
        for column_index in range(worksheet.ncols):
            output_worksheet.write(row_index, column_index, worksheet.cell_value(row_index, column_index))
output_workbook.save(output_file)