

import sys

def main():
    n = int(sys.stdin.readline().strip())
    printers = 0
    days = 0
    while True:
        if printers >= n:
            break
        days += 1
        printers += 1
    print(days)

if __name__ == '__main__':
    main()
