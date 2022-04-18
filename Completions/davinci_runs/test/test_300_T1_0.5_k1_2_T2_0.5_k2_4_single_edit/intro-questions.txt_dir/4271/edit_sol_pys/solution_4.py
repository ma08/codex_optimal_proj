

import math

a, b, c = map(int, input().split())


def f(x):
    return a * x + b * math.sin(c * x * math.pi)


def f_inverse(x):
    return ((x - b * math.sin(c * math.pi)) / a) / (c * math.pi)


def binary_search(l, r, f, target):
    while l < r:
        c = (l + r) / 2
        if f(c) >= target:
            r = c
        else:
            l = c
    return l


def ternary_search(l, r, f, target):
    while r - l > 1e-9:
        c1 = (2 * l + r) / 3
        c2 = (l + 2 * r) / 3
        if f(c1) > f(c2):
            l = c1
        else:
            r = c2
    return (l + r) / 2


def ternary_search_inverse(l, r, f, target):
    while r - l > 1e-9:
        c1 = (2 * l + r) / 3
        c2 = (l + 2 * r) / 3
        if f(c1) > target:
            l = c1
        else:
            r = c2
    return (l + r) / 2


def calc_area(l, r, f):
    return (f(r) + f(l)) * (r - l) / 2


l = 0
r = 100
print(ternary_search_inverse(l, r, f_inverse, 100))
