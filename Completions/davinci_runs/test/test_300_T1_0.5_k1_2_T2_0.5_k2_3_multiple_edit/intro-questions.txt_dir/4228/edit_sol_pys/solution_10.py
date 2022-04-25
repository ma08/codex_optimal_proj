n, l = map(int, input().split())
tastes = [l + i for i in range(n)]
print(sum(tastes) - min([abs(f) for f in tastes]))

