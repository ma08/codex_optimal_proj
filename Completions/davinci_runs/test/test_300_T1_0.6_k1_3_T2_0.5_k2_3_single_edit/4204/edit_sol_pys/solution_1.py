
from math import log

def get_digit(n,k):
    if k <= len(n): return n[k-1]
    for i,c in enumerate(n):
        k -= (int(c)*(10**(i+1))) 
        if k <= 0: return int(c)%10

n = input()
k = int(input())

print(get_digit(n,k))
