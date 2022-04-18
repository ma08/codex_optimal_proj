
a, b, k = map(int, input().split())

if a > b:
    a, b = b, a

for i in range(k):
    if a > 0:
        a -= 1
    elif b > 0:
        b -= 1

print(a, b)
