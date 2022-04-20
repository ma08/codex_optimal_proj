

import sys, math

def main():
    a, b = map(int, sys.stdin.readline().split())
    print(math.ceil(a / b))

if __name__ == '__main__':
    main()
