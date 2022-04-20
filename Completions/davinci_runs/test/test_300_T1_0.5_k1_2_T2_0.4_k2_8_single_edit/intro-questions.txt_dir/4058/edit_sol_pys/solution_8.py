

import sys

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        m, k = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        b = list(map(int, sys.stdin.readline().split()))
        a.sort()
        b.sort()
        i = 0
        j = 0
        ans = 0
        while i < m and j < m:
            if a[i] <= b[j]:
                i += 1
            else:
                j += 1
                ans += 1
        print(ans)

if __name__ == '__main__':
    main()
