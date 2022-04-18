

n, L = map(int, input().split())

flavors = [L + i for i in range(n)]

print(sum(flavors) - min([abs(f) for f in flavors]))
