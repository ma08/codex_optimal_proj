

a, b, c = map(int, input().split())  # a = bottle 1, b = bottle 2

if b + c > a:
    print(b + c - a)
else:
    print(0)
