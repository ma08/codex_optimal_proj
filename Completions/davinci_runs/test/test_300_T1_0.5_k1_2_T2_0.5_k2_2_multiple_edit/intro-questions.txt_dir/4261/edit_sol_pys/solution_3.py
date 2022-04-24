

# a = bottle 1, b = bottle 2, c = bottle 3, d = bottle 4
a, b, c, d = map(int, input().split())

if b + c + d > a:
    print(b + c + d - a)
else:
    print(0)
