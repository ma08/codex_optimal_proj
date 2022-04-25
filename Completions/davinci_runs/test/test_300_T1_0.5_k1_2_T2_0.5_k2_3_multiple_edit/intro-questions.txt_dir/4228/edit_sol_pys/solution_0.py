
n, m = map(int, input().split())
flavors = [m + i for i in range(n)]

print(sum(flavors) - min([abs(f) for f in flavors]))
