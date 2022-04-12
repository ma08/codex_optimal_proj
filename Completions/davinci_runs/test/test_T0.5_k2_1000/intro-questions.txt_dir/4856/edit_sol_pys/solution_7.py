

a, b = input().split()  # split a and b

if int(a[::-1]) > int(b[::-1]):
    print(a[::-1])
else:
    print(b[::-1])
