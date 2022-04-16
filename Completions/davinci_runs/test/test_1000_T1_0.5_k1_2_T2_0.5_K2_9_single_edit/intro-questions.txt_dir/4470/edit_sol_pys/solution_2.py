

# import math

# def calculate(n):
#     if n == 1:
#         return 0

#     if n % 2 == 0:
#         return 1 + calculate(n/2)
#     if n % 3 == 0:
#         return 1 + calculate(2*n/3)
#     if n % 5 == 0:
#         return 1 + calculate(4*n/5)
#     return -1

# q = int(input())

# for i in range(q):
#     n = int(input())
#     print(calculate(n))


import math

def calculate(n):
    if n == 1 or n == 0:
        return 0, 1

    steps = 1
    if n % 2 == 0: 
        steps += 1 + calculate(n/2)
    if n % 3 == 0: 
        steps += 1 + calculate(2*n/3)
    if n % 5 == 0: 
        steps += 1 + calculate(4*n/5)
    return steps

q = int(input())

for i in range(q):
    n = int(input())
    print(calculate(n)[0])
