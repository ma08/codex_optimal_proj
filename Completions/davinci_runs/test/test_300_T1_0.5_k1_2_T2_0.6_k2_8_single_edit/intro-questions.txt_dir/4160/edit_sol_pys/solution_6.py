

import math

a = float(input())
b = float(input())
c = float(input())

D = b ** 2 - 4 * a * c

if D < 0:
    print("No roots")
elif D == 0:
    x = -b / (2 * a)
    print("One root: " + str(x))
else:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("Two roots: " + str(x1) + " and " + str(x2))
