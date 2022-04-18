
import sys

def main():
    n = int(sys.stdin.readline().strip())
    printers = 1
    days = 0
    while (printers < n):
        days += 1
        printers += printers
    print(days)

if __name__ == '__main__':
    main()
