

import sys

def main():
    a, b, c = map(int, sys.stdin.readline().split())
    print(min(b // a, c))

if __name__ == '__main__':
    main()