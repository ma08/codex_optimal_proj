import math
def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
n,m=map(int,input().split())
a=list(map(int,input().split()))
for i in range(m):
    if isPrime(a[i]):
        print(a[i])
    else:
        print(a[i]//a[n+i])
