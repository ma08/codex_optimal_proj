

k = int(input())

a = 1
b = 2

for i in range(k):
    a, b = b, a+b

print(a, b)
