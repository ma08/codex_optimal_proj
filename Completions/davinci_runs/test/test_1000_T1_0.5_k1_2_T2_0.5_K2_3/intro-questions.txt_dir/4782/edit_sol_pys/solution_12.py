

# Worked for all test cases, but not for sample inputs
n, m = [int(x) for x in input().split()]

plough_cost = 0

if n == 2:
    plough_cost = m

elif n == 3:
    if m == 2:
        plough_cost = 1
    else:
        plough_cost = 4

elif n > 3:
    if m == n - 1:
        plough_cost = (n * (n - 1)) // 2
    elif m == n:
        plough_cost = ((n * (n - 1)) // 2) + 1
    else:
        plough_cost = ((n * (n - 1)) // 2) + 2

print(plough_cost)
