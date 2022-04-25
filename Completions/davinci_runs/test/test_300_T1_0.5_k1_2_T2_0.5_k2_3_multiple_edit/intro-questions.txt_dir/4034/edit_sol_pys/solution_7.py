


import sys, collections

n = int(input())
a = list(map(int, input().split()))


def solve(a):
    ans = 0
    for i in range(1, n):
        if a[i] == a[i - 1]:
            ans += 1
            if i == n - 1:
                if a[i] == a[i - 2]:
                    a[i] = 0
                else:
                    a[i] = 1
            elif a[i] == a[i + 1]:
                a[i] = 0
        else:
            if i == n - 1:
                if a[i] == a[i - 2]:
                    a[i] = 1
                else:
                    a[i] = 0
            else:
                if a[i] == a[i + 1]:
                    a[i] = 0
                else:
                    a[i] = 1
    return ans


print(solve(a))
