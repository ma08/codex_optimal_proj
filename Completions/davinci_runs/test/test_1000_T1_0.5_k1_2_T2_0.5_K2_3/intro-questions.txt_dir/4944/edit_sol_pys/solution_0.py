
import sys

def main():
    n = int(sys.stdin.readline().strip()) # number of pages to print
    printers = 1
    days = 0
    while True:
        if printers >= n:
            break
        days += 1
        printers += printers # add the number of pages printed the previous day to the total
    print(days)

if __name__ == '__main__':
    main()
