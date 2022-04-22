

# a = bottle 1, b = bottle 2, c = bottle 3
a, b, c = map(float, input().split())

print(max(0, b + c - a))
