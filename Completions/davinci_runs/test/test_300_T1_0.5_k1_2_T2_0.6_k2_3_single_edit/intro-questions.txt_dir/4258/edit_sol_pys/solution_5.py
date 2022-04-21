import csv
import os


def file_read(filename):
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            print(row)
            print(row[0])
            print(row[0], row[1], row[2],)


print(file_read("file.csv"))
