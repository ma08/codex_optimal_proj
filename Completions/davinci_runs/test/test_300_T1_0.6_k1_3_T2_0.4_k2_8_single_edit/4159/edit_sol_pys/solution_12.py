
a, b, k = map(int, input().split())

for i in range(k):
    if a > b:
        a -= 1 if a > 0 else 0
    else:
        b -= 1 if b > 0 else 0

print(a, b)
