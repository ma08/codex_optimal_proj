

n, l = map(int, input().split()) # n = 3, l = -1

flavors = [l + i for i in range(n)] # l = -1, i = 0, 1, 2

print(sum(flavors) - min([abs(f) for f in flavors])) # -1 + 0 + 1 + 2 - min(1, 2, 0)
