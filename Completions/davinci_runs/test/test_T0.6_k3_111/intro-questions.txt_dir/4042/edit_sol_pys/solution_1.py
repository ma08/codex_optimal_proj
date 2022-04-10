
import math

x = float(input())

# round to 3 digits
x *= 1000

a = x // 100
b = x % 100

# find the two closest integers that sum to a
a_1 = math.ceil(a/2)
a_2 = math.floor(a/2)

# find the two closest integers that sum to b
b_1 = math.ceil(b/2)
b_2 = math.floor(b/2)

# if a_1 + a_2 == a, but b_1 + b_2 != b, then b_1 and b_2 are too far apart
# and we need to adjust them
if a_1 + a_2 == a and b_1 + b_2 != b:
    if b_1 > b_2:
        b_1 -= 1
    else:
        b_2 -= 1

# if a_1 + a_2 != a, but b_1 + b_2 == b, then a_1 and a_2 are too far apart
# and we need to adjust them
if a_1 + a_2 != a and b_1 + b_2 == b:
    if a_1 > a_2:
        a_1 -= 1
    else:
        a_2 -= 1

# if a_1 + a_2 != a, and b_1 + b_2 != b, then a_1 and a_2 are too far apart,
# and we need to adjust them
if a_1 + a_2 != a and b_1 + b_2 != b:
    if a_1 > a_2:
        a_1 -= 1
    else:
        a_2 -= 1

print(a_1, a_2)
