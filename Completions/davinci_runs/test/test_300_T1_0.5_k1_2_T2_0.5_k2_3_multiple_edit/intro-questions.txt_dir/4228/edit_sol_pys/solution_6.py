
n, l = map(int, input().split())

tastes = [l + i for i in range(n)]

print(sum(tastes) - min(tastes, key=lambda x: abs(x)))
