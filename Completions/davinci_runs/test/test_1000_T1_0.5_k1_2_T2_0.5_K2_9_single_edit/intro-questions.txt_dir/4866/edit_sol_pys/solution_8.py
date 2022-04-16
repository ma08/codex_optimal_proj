

import sys

def main():
    for line in sys.stdin:
        month, day = line.split()
        if month == 'OCT' and day == '31' or month == 'DEC' and day == '25' :
            print('yup')
        else:
            print('nope')

if __name__ == '__main__':
    main()
