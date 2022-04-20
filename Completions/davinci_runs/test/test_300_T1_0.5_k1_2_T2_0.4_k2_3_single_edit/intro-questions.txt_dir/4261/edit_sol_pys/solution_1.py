

# a = bottle 1, b = bottle 2, c = bottle 3
a, b, c = map(int, input().split())

if a + b > c:
    print(a + b - c)
else:
    print(0)
