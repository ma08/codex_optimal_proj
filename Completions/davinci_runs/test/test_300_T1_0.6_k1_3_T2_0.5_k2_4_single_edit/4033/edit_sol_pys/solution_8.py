

def main():
    import sys
    import math
    # define the recurrence relation
    def f(n,a,b):
        if n==0:
            return 0
        if (n,a,b) in d:
            return d[(n,a,b)]
        else:
            d[(n,a,b)]=min(a*n+f(n-1,a,b),b*n+f(n-1,a,b),a*b+f(n-1,a-1,b-1))
            return d[(n,a,b)]
    a,b=map(int,sys.stdin.readline().split())
    n=(a+b)//2
    d=dict()
    print(f(n,a,b))
main()
