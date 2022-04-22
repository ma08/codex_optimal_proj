
# a = bottle 1, b = bottle 2
a, b, c = map(int, input().split())

if a - b > c:
    print(c - (a - b))
else:
    print(0)
