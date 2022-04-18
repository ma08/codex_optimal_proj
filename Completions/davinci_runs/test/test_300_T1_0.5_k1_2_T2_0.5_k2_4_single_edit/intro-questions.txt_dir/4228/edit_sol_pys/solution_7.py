

n, l = map(int, input().split())  # n, l = (5, -4)

flavors = [l + i for i in range(n)]  # flavors = [-4, -3, -2, -1, 0]

print(sum(flavors) - min([abs(f) for f in flavors]))
