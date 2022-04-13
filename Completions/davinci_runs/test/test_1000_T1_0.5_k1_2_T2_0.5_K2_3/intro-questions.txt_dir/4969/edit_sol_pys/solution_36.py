from math import pi, acos, sin, cos

def solve(r, c):
    A = pi * r * r
    B = pi * c * c

    return A/B * 100

def solve2(a, b, c):
    # cos(C) = (a^2 + b^2 - c^2) / 2ab
    # C = acos((a^2 + b^2 - c^2) / 2ab)

    C = acos((a*a + b*b - c*c) / 2*a*b)

    return C

def solve3(a, b, c):
    # sin(C) = c / b
    # C = asin(c / b)

    C = asin(c/b)

    return C

print(solve(10, 4))
print(solve2(10, 4, 6))
print(solve3(10, 4, 6))
