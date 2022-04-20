

# read input
a, b, c = map(int, input().split())

# calculate amount of water in bottle 2
bottle2 = c - (a - b)

# print result
print(max(0, bottle2))
