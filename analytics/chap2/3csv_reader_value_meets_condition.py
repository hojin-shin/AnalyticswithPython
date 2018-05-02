#!python
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline = '') as csv_in_file:
    with open(output_file, 'w', newline = '') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            supplier = str(row_list[0]).strip()
            cost = str(row_list[3]).strip('$').replace(',','')
            if supplier == 'Supplier X' and float(cost) > 600.00:
                filewriter.writerow(row_list)
                print(row_list)
