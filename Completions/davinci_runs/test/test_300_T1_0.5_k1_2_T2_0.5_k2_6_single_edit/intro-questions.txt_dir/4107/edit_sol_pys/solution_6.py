

from itertools import combinations


def solve(n, k, s):
    cost = 0
    for i in range(1, n + 1):
        if s[i - 1] == '1':
            cost += i
            continue
        if i - k - 1 >= 0 and s[i - k - 1] == '1':
            continue
        if i + k - 1 < n and s[i + k - 1] == '1':
            continue
        cost += i
    return cost


n, k = [int(x) for x in input().split()]
s = input()

print(solve(n, k, s))
