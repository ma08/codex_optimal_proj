k = int(input())

a = 0
b = 0
for i in range(k):
    if i == 0:
        b = 1
    elif i == 1:
        b = 1
        a = 1
    else:
        temp = b
        b = a + b
        a = temp

print(a, b)
