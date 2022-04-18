

import sys

def main():
    n = int(sys.stdin.readline())
    l = list(map(int, sys.stdin.readline().split()))
    l.sort()
    print(l[0])

if __name__ == '__main__':
    main()
