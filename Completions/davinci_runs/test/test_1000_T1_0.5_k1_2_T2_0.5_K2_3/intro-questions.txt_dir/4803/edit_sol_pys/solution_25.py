import math

def f(x):
    return math.pow(x, x) - N

def main():
    N = float(input())

while b - a > 1e-5:
    c = (a + b) / 2
    if f(c) > 0:
        b = c
    else:
        a = c
print(a)
