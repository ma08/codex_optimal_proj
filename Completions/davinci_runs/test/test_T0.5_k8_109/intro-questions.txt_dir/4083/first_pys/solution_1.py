

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    a.sort()
    print(a)

    ans = 0
    while a[0] < a[-1]:
        a[0] //= 2
        a.sort()
        ans += 1

    print(ans)

main()