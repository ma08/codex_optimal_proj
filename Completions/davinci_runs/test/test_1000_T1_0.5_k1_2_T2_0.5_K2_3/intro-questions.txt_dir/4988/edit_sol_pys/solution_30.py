#!/usr/bin/env python3

def factorial(n): 
    if n < 0: 
        return 0
    elif n == 0 or n == 1: 
        return 1
    else: 
        return n * factorial(n-1) 

for _ in range(int(input())): 
    print(factorial(int(input())) % 10)
