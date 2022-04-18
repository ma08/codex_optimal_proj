

import sys

def main():
    n = int(sys.stdin.readline())
    a = map(int, sys.stdin.readline().split())
    a.sort()
    a.reverse()
    print a[0] + a[1] + 1

if __name__ == "__main__":
    main()