

# a = bottle 1, b = bottle 2, c = bottle 3
a, b, c = map(int, input().split())

if b + c > a:
    print(b + c - a, end='')
else:
    print(0, end='')
