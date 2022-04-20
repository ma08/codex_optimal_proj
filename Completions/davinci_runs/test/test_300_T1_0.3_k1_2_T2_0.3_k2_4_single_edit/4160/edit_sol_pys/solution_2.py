

x = int(input('Enter the number: '))

a = 0
b = 100

while b < x:
    b += b // 100
    a += 1

print(a)
