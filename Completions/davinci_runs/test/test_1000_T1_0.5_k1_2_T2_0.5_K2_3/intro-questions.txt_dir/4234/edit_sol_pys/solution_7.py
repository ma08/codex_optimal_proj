# coding: utf-8
import sys
from collections import defaultdict

def main():
    n, m = map(int, input().split())
    cnt = defaultdict(int)
    for i in range(n):
        a, b = map(int, input().split())
        cnt[a] += 1
        cnt[b+1] -= 1
    ans = 0
    cur = 0
    for i in range(1, m+1):
        cur += cnt[i]
        if cur == n:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
