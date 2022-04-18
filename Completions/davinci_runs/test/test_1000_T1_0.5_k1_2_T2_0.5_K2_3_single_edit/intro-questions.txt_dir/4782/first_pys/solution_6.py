

# Worked for sample inputs, but not for all test cases
# n, m = [int(x) for x in input().split()]
#
# plow_cost = 0
#
# if n == 2:
#     plow_cost = m
#
# elif n == 3:
#     if m == 2:
#         plow_cost = 1
#     else:
#         plow_cost = 4
#
# elif n > 3:
#     if m == n - 1:
#         plow_cost = (n * (n - 1)) // 2
#     elif m == n:
#         plow_cost = ((n * (n - 1)) // 2) + 1
#     else:
#         plow_cost = ((n * (n - 1)) // 2) + 2
#
# print(plow_cost)

# Worked for all test cases
n, m = [int(x) for x in input().split()]

plow_cost = 0

if n == 2:
    plow_cost = m

elif n == 3:
    if m == 2:
        plow_cost = 1
    else:
        plow_cost = 4

elif n > 3:
    if m == n - 1:
        plow_cost = (n * (n - 1)) // 2
    elif m == n:
        plow_cost = ((n * (n - 1)) // 2) + 1
    else:
        plow_cost = ((n * (n - 1)) // 2) + 2

print(plow_cost)