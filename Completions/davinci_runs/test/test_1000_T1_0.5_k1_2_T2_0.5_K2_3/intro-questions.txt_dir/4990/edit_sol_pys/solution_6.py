

a, b, c = map(int, input().split()) 
if b >= a:
    print(1)
else:
    print(a // (c - 1) + 1 if a % (c - 1) != 0 else a // (c - 1))
