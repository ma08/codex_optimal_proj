

import sys

def main():
    x = float(sys.stdin.readline())
    a = int(round(x, 0)) # noqa
    b = int(round(x * 10, 0)) - a * 10 # noqa
    print(a, b)

if __name__ == '__main__':
    main()
