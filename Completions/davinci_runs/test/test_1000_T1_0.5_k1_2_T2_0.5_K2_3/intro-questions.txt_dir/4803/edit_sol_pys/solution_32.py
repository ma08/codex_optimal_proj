import math
N = float(input("Enter the number: "))

def f(x):
    return x**x - N

a = 0.01
b = N

while b - a > 1e-6:
    c = (a + b) / 2
    if f(c) > 0: # если на середине интервала значение функции больше нуля
        b = c
    else: # иначе значение функции меньше нуля
        a = c

print("The result is:", a)
