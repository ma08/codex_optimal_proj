
n, l = map(int, input().split())  # n: number of flavors, l: leftmost flavor

flavors = [l + i for i in range(n)]  # list of flavors

print(sum(flavors) - min([abs(f) for f in flavors]))
