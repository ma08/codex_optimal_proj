

def main():
    import sys
    import math
    for line in sys.stdin:
        a,b=map(int,line.split())
        n=(a+b)//2
        d={}
        # define the recurrence relation
        def f(n,a,b):
            if n==0:
                return 0
            if (n,a,b) in d:
                return d[(n,a,b)]
            else:
                d[(n,a,b)]=min(a*n+f(n-1,a,b),b*n+f(n-1,a,b),a*b+f(n-1,a-1,b-1))
                return d[(n,a,b)]
        print(f(n,a,b))
main()
