#!usr/bin/env python3
import pandas as pd 
import sys

#특정조건을 충족하는 행의 필터링 for pandas 
input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2013', index_col = None)  #필터링 대상 sheet open
#조건필터 열과 항목 설정
data_frame_value_meets_condition = data_frame[data_frame['Sale Amount'].astype(float) >1500.0]

writer = pd.ExcelWriter(output_file)
data_frame_value_meets_condition.to_excel(writer, sheet_name = 'jan_13_ouput', index=False)
writer.save()
