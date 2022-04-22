
# a = bottle 1, b = bottle 2
a, b, c, d = map(int, input().split())

if c + d > a:
    print(c + d - a)
elif c + d > b:
    print(c + d - b)
else:
    print(0)
