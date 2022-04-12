import math

n = float(input("Enter a number: "))

def f(x, n):
    return math.pow(x, x) - n 

a = 0.5
b = 2

while b - a > 1e-5:
    c = (a + b) / 2
    if f(c, n) > 0:
        b = c
    else:
        a = c

print("The root of the equation is: ", a)
