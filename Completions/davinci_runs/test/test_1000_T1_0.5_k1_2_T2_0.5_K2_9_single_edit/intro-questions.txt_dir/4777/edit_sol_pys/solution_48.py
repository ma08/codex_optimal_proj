

k = int(input())
a, b = 0, 1

for i in range(k):
    a, b = b, a + b

print(a, b)
