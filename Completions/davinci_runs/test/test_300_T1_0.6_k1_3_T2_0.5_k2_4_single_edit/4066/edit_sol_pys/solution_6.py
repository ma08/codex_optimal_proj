

from gcd import *

def lcm(x,y):
    return x*y/gcd(x,y)


def minimum_lcm(A):
    minimum = lcm(A[0],A[1])
    a = A[0]
    b = A[1]
    for i in range(0,len(A)-1):
        for j in range(i+1,len(A)):
            if lcm(A[i],A[j])<minimum:
                minimum = lcm(A[i],A[j])
                a = A[i]
                b = A[j]
    return a,b

if __name__=="__main__":
    n = int(input())
    A = map(int,input().split())
    print minimum_lcm(A)
