

n, l = map(int, input().split())

flavors = [l + i for i in range(n)]

print(sum(flavors) - min([abs(f) for f in flavors]))