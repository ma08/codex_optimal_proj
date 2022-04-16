

a = int(input())
b = 1
while a > 9:
    c = a % 10
    if c > 0:
        b *= c
    a //= 10
print(b * a)
