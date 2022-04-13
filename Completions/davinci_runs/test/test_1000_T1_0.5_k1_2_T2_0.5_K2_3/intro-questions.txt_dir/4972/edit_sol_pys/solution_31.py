
import sys
import math
import os
import csv
def main():
    #x = sys.stdin.readline().strip()
    #print(x)
    f = open('test.csv', 'rt')
    try:
        reader = csv.reader(f)
        for row in reader:
            print row
    finally:
        f.close()

if __name__ == '__main__':
    main()
