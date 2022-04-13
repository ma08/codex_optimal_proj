
k = int(input())

a = 1
b = 1
c = 0

for i in range(k):
    c = b
    b = a + c
    a = c

print(a, b)
