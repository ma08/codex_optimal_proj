

import sys

def main():
    x = float(sys.stdin.readline())
    a = round(x, 0)
    b = round(x * 10, 0) - a * 10
    print(a, b)

if __name__ == '__main__':
    main()
