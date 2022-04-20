

import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    d = {}
    for i in range(n):
        d[a[i]] = i
    a.sort()
    for i in range(n):
        print(d[a[i]]+1)

if __name__ == "__main__":
    main()
