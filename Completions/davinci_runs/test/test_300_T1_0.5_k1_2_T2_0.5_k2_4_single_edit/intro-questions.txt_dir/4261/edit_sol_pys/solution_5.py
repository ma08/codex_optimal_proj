

# a = bottle 1, b = bottle 2, c = bottle 3
a, b, c, d = map(int, input().split())

if b + d > a:
    print(b + d - a)
else:
    print(0)
