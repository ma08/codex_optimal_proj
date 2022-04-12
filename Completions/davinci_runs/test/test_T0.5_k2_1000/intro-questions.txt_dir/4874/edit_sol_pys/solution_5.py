# https://codeforces.com/problemset/problem/1238/B

from collections import defaultdict

def solve():
    n = int(input())
    s = input()
    d = defaultdict(int)
    for i in range(n):
        d[s[i]] += 1

    if len(d) == 1:
        print(0)
        return

    min_count = n
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] != s[j]:
                count = 0
                for k in range(i, j + 1):
                    if s[k] != s[i] and s[k] != s[j]:
                        count += 1
                min_count = min(min_count, count)

    print(min_count)

t = int(input())
for _ in range(t):
    solve()
