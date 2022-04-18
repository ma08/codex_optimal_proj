

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    a.sort()
    b.sort()

    i = 0
    j = 0
    count = 0
    while i < n and j < m:
        if a[i] <= b[j]:
            count += 1
            i += 1
        j += 1
    print(count)

if __name__ == '__main__':
    main()
