# https://atcoder.jp/contests/abc156/tasks/abc156_c


# input

n, m = map(int, input().split())
x = list(map(int, input().split()))

x.sort()

if x[-1] > n:
    print(-1)
    exit()

ans = 10 ** 9
for p in range(n):
    s = 0
    for i in range(m):
        s += (x[i] - p) ** 2
    ans = min(s, ans)

print(ans)
