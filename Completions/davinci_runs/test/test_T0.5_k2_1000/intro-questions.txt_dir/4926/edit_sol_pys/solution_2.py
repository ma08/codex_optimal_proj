
#Solution: 

import math

def factorial(n):
    if n == 0:
        return 1.0
    return n*factorial(n-1)

def e_approx(n):
    approx = 0
    for i in range(n+1):
        approx += 1/factorial(i)
    return approx

def main():
    n = int(input())
    print(e_approx(n))

main()
