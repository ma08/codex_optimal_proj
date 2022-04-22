

# a = bottles 1, b = bottles 2, c = bottles 3
a, b, c = map(int, input().split())

if b + c > a:
    print(b + c - a)
else:
    print(0)
