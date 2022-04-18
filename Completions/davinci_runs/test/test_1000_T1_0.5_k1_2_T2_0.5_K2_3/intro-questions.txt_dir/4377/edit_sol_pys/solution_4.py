

A, B, C, D = map(int, input().split())

a = max(A, B, C, D)
b = A + B + C + D - a
c = min(A, B, C, D)

print(a - c, b - c, c)
