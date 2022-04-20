
n = int(input())
a = list(map(int, input().split()))
d = dict(zip(a, [a.count(i) for i in a]))

ans = 0
for i in d:
    ans += d[i] - 2

print(ans)
