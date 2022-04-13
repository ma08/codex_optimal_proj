
from math import sqrt
 
n = int(input())
 
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
 
for i in range(n):
    if is_prime(i):
        print(i)
