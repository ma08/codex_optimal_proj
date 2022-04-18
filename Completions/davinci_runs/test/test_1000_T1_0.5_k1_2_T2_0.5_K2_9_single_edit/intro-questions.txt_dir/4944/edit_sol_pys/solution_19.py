
import sys

def main():
    n = int(sys.stdin.readline().strip())
    printer = 1
    days = 0
    while True:
        if printer >= n:
            break
        days += 1
        printer += printer
    print(days)

if __name__ == '__main__':
    main()
