
k = int(input())
a, b = 0, 1

for i in range(k):
    if i == 0:
        pass
    elif i == 1:
        a = 1
    else:
        a, b = b, a + b

print(a, b)
