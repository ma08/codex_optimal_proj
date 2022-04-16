

import sys

def main():
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        print('GREATER')
    elif a < b:
        print('LESS')
    else:
        print('EQUAL')

if __name__ == '__main__':
    main()
