

a, b = input().split()
a = a[::-1]
b = b[::-1]
print(int(a) if int(a) > int(b) else int(b))
