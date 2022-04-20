

import sys

def main():
    n, l = map(int, sys.stdin.readline().rstrip().split())  # n, l = (int(x) for x in input().split())
    print(sum(range(l, l+n)))

if __name__ == '__main__':
    main()
