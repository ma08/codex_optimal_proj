

a, b = map(int, input().split())
m, sigma = map(int, input().split())

max_rent = 0

for x in range(1, m//2 + 1):
    y = m - x
    if(2*x + y >= sigma):
        rent = a*x + b*y
        if(rent > max_rent):
            max_rent = rent

print(max_rent)
