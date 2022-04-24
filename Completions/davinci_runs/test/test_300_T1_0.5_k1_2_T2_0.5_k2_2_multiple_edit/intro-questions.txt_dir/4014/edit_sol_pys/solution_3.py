
import re
import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    l = 0
    r = n - 1
    ans = [0] * n
    for i in range(n):
        if a[l] > a[r]:
            ans[i] = a[l]
            l += 1
        else:
            ans[i] = a[r]
            r -= 1

    print(' '.join(map(str, ans)))


if __name__ == "__main__":
    main()
