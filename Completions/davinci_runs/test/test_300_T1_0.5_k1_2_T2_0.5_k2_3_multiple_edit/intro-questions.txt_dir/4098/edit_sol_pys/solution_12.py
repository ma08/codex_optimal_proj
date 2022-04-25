# coding=utf-8
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem


# n, k = map(int, raw_input().split())
# a = list(map(int, raw_input().split()))

# n, k = 5, 2
# a = [1, 2, 15, 15, 15]
# n, k = 6, 1
# a = [36, 4, 1, 25, 9, 16]
# n, k = 4, 4
# a = [1, 10, 100, 1000]


def is_valid(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    l = list(d.values())
    l.sort()
    print(l)
    if len(l) == 1:
        return True
    elif len(l) == 2:
        if l[0] == 1 and l[1] == l[0] + 1:
            return True
        elif l[1] == 1 and l[0] == l[1] + 1:
            return True
        else:
            return False
    else:
        return False


def solve(a, k):
    a.sort()
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j]
            t = 1
            for l in range(1, i):
                if abs(a[i - 1] - a[i - l - 1]) <= 5:
                    t += 1
                else:
                    break
            dp[i][j] = max(dp[i][j], dp[i - t][j - 1] + t)
    return dp[n][k]


# print(solve(a, k))

# s = raw_input()
s = 'abcdefghhgfedecba'
print(is_valid(s))
