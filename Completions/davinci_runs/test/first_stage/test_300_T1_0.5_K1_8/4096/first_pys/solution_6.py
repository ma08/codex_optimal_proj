

import sys

def main():
    n, m = map(int, sys.stdin.readline().strip().split())
    a = map(int, sys.stdin.readline().strip().split())
    a.sort()
    a.reverse()
    for i in range(1, n+1):
        a[i-1] -= i-1
    a.sort()
    a.reverse()
    if a[0] < m:
        print -1
    else:
        print (m + a[0] - 1) / a[0]

if __name__ == "__main__":
    main()