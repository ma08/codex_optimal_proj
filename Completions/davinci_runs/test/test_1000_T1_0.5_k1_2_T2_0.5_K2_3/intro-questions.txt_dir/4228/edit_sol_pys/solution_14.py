
n, l = map(int, input().split()) # n: number of flavors, l: initial position
flavors = [l + i for i in range(n)]

print(sum(flavors) - min(flavors, key=abs))
