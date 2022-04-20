

import sys

def main():
    k = int(sys.stdin.readline())
    a, b = map(int, sys.stdin.readline().split())
    for i in range(a, b + 1):
        if i % k == 0:
            print("OK")
            sys.exit()
    print("NG")


if __name__ == '__main__':
    main()
