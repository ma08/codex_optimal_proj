

import sys

def main():
    n, k, m = map(int, sys.stdin.readline().rstrip().split())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    ave = (sum(a)+m*n)/n
    if ave > k:
        print(-1)
    else:
        print(int(k-ave))

if __name__ == '__main__':
    main()