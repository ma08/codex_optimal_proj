
from math import factorial
from sys import stdin

def choose(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

def prob(n):
    return sum(choose(n, i) / n**i for i in range(n))

print(prob(int(stdin.readline())))
