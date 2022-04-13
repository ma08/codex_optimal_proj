
import math
N = int(input())

e = 1
for n in range(1, N + 1):
    e += 1 / math.factorial(n)  # factorial is a function in the math module

print(e)
