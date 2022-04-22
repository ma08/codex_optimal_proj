
# a = bottles 1, b = bottles 2
a, b, c = map(int, input().split())

if b + c < a:
    print(a - b - c)
else:
    print(0)
