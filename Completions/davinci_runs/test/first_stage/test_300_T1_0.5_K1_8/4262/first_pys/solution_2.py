

#N = int(input())
#P = list(map(int, input().split()))
#Q = list(map(int, input().split()))

N = 3
P = [1, 3, 2]
Q = [3, 1, 2]

#print(N)
#print(P)
#print(Q)

import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def nPr(n, r):
    return factorial(n) / factorial(n - r)

def permutation_index(permutation):
    index = 0
    n = len(permutation)
    for i in range(n):
        index += nPr(n - i - 1, 1) * permutation[i]
    return index

print(abs(permutation_index(P) - permutation_index(Q)))