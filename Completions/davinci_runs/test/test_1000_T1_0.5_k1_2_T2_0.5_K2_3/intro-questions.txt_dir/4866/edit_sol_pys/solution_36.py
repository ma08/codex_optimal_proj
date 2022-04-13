
'''
# SOLUTION

import sys
import calendar
import datetime

month_index = {'JAN':1, 'FEB':2, 'MAR':3, 'APR':4, 'MAY':5, 'JUN':6, 'JUL':7, 'AUG':8, 'SEP':9, 'OCT':10, 'NOV':11, 'DEC':12}

def main():
    date = sys.stdin.readline().strip().split(' ')
    month = month_index[date[0]]
    day = int(date[1])

    if (month == 10 and day == 31) or (month == 12 and day == 25):
        print('yup')
    else:
        print('nope')

if __name__ == '__main__':
    main()
'''
