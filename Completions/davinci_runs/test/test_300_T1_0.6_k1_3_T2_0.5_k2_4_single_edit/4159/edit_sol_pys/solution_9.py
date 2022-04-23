
a, b, k = map(int, input().split())

for i in range(k):
    if a > 0:
        a -= 1
    elif b > 0:
        b -= 1

print(a, b)
