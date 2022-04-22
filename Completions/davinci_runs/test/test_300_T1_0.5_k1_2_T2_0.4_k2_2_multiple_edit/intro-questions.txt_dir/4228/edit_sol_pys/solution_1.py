
n, l = map(int, input().split())

flavors = [l + i for i in range(1, n + 1)]

print(sum(flavors) - min(flavors, key=lambda x: abs(x)))
