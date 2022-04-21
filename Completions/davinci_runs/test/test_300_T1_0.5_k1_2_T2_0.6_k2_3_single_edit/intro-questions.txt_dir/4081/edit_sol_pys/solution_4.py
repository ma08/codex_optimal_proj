

import sys

sys.setrecursionlimit(10 ** 7)


def problem_C2():
    def read():
        n = int(input())
        a = list(map(int, input().split()))
        return n, a

    def f(x):
        if x == 0:
            return 0
        if x == p[m]:
            return m
        l, r = 0, m
        while l < r:
            mid = (l + r) // 2
            if p[mid] < x:
                l = mid + 1
            else:
                r = mid
        return l

    now = 0
    for i in range(n):
        if a[i] > now:
            ans.append('R')
            now = a[i]
        else:
            x = f(p[now] - i)
            if x > now:
                ans.append('R')
                now = x
            else:
                ans.append('L')
    print(len(ans))
    print(''.join(ans))


problem_C2()
