
import csv


csvfile = open('/Users/aishwaryashekhar/Downloads/test.csv', 'r')
reader = csv.reader(csvfile, delimiter=',')

for row in reader:
    print(row)
