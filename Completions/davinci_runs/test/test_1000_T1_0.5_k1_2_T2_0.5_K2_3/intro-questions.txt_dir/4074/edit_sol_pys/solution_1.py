# https://codeforces.com/contest/1362/problem/A

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if n < k:
        print(1)
    else:
        print(n // k + n % k)
