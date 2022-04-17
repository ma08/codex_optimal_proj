

#-----main-----

a, b = map(int, input().split()) # split input into multiple numbers

if a <= b:
    print(0)
else:
    print(a - b)
