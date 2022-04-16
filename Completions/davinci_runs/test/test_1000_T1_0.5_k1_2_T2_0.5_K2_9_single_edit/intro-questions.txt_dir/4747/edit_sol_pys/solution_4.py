

#Die, k-times 

from math import factorial

def n_choose_k(n,k):
    return factorial(n)/(factorial(n-k)*factorial(k))

def expected_value(n,k):
    if k == 1:
        return (n+1)/2
    else:
        return ((n+1)/2)*(1-n_choose_k(n,k)/n_choose_k(n+k-1,k)) + expected_value(n,k-1)

n, k = [int(x) for x in input().split()]
print(expected_value(n,k))
