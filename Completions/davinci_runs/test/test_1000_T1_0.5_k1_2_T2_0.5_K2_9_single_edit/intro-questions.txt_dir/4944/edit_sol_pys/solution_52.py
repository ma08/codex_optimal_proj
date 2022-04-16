

import sys

def main():
    n = int(sys.stdin.readline().strip())
    printers = 1
    days = 0
    while True:
        if printers >= n:
            break
        days += 1
        printers += printers
    print(days + 1)

if __name__ == '__main__':
    main()
