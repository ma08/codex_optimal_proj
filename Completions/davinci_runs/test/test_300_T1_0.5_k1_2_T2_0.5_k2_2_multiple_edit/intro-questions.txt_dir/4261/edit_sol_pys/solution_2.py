

a, b, c = map(int, input().split())  # map(function, iterable)
if a > b:
    print(c - (a - b))
else:
    print(c + (b - a))
