import itertools

n, a = map(int, input().split())  # n:個数
x = list(map(int, input().split()))  # x:各個数

ans = 0
for i in range(1, n+1):
    for j in itertools.combinations(x, i):
        if sum(j) / i == a:
            ans += 1
print(ans)
