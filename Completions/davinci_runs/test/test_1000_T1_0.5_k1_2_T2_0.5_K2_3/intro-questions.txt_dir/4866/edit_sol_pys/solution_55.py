

# SOLUTION

import sys

month_index = {'JAN':1, 'FEB':2, 'MAR':3, 'APR':4, 'MAY':5, 'JUN':6, 'JUL':7, 'AUG':8, 'SEP':9, 'OCT':10, 'NOV':11, 'DEC':12, 'JANUARY':1, 'FEBRUARY':2, 'MARCH':3, 'APRIL':4, 'MAY':5, 'JUNE':6, 'JULY':7, 'AUGUST':8, 'SEPTEMBER':9, 'OCTOBER':10, 'NOVEMBER':11, 'DECEMBER':12}

def main():
    date = sys.stdin.readline().strip().upper().split(' ')
    month = month_index[date[0]]
    day = date[1].strip(',')
    day = int(day)

    if (month == 10 and day == 31) or (month == 12 and day == 25):
        print('yup')
    else:
        print('nope')

if __name__ == '__main__':
    main()
