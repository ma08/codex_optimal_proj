

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
s = [0] * (n + 1)
for i in range(n):
    s[i + 1] = s[i] + a[i]
for i in range(m):
    l, r = map(int, input().split())
    print(s[r] - s[l - 1])
