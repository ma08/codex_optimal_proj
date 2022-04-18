
#This is a test file
#Solution :

import math

def factorial(x):
    if x == 0:
        return 1
    else:
        return x*factorial(x-1)

def e_approx(n):
    approx = 0
    for i in range(n+1):
        approx += 1/factorial(i)
    return approx

def main():
    n = int(input())
    print(e_approx(n))

main()
