
k = int(input('Enter number: '))

a = 1
b = 1

for i in range(k):
    temp = b
    b = a + b
    a = temp

print(a, b)
