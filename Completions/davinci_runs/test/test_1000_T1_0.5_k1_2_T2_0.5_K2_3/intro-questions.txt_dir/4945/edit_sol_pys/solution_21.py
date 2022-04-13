

a, b = map(int, input().split())
m, s = map(int, input().split())

max_rent = 0
for y in range(1, m//2 + 1):
    x = s - 2*y
    if x >= 1:
        max_rent = max(max_rent, a*x + b*y)

print(max_rent)
