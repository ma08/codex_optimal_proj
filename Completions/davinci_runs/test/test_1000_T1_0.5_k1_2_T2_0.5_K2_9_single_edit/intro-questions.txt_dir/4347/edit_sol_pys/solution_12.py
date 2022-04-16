
#!/bin/python3
#Solution

n = int(input())

def factorial(n) :
    if n == 0 :
        return 1 
    else :
        return n * factorial(n - 1) 

print(factorial(n) // (factorial(n // 2) ** 2)) 
