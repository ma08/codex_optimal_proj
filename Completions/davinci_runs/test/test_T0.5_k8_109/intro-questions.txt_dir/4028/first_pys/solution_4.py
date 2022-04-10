

#from math import factorial
#from collections import Counter

#def nCr(n,r):
#    f = factorial(n)
#    f /= factorial(r)
#    f /= factorial(n-r)
#    return f

#def nPr(n,r):
#    f = factorial(n)
#    f /= factorial(n-r)
#    return f

#def nCrModp(n, r, p): 
#    numerator = 1
#    for i in range(r): 
#        numerator = (numerator * (n - i)) % p  
#    denominator = 1
#    for i in range(1, r + 1): 
#        denominator = (denominator * i) % p 
#    return (numerator * pow(denominator, p - 2, p)) % p

#def nPrModp(n, r, p): 
#    numerator = 1
#    for i in range(r): 
#        numerator = (numerator * (n - i)) % p  
#    return numerator

#def modinv(a, m):
#    for x in range(1, m) : 
#        if ((a * x) % m == 1) : 
#            return x 
#    return 1

def solve(n,s):
    #code here
    return 0

MOD = 10**9 + 7

if __name__ == "__main__":
    n = int(input())
    s = input()
    print(solve(n,s))