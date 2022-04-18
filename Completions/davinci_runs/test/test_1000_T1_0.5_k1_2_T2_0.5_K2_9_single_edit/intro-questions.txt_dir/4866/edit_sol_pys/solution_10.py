

import sys

def main():
    line = sys.stdin.readline().strip().split(' ')
    month = line[0]
    day = line[1]

    if (month == 'OCT' and day == '31') or (month == 'DEC' and day == '25'):
        print('yup')
    else:
        print('nope')

if __name__ == '__main__':
    main()
