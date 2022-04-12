

a, b = map(int, input().split()) # a = 1, b = 2
m, sum = map(int, input().split()) # m = 3, sum = 4

max_rent = 0
for y in range(1, m//2 + 1): # y = 1, 2
    x = sum - 2*y
    if x >= 1: # x = 1, 2
        max_rent = max(max_rent, a*x + b*y)

print(max_rent)
