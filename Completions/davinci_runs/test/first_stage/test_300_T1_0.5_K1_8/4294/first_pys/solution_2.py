

import sys

def main():
    x, a = map(int, sys.stdin.readline().strip().split())
    if x < a:
        print(0)
    else:
        print(10)

if __name__ == '__main__':
    main()