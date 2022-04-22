import math


def isPrime(n):
    if n==1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i==0:
            return False
    return True

n = int(input())
if isPrime(n):
    print(1)
elif isPrime(n-2):
    print(2)
else:
    print(3)
