import sys

def solve(n, t):
    t.sort()
    t1 = t[:n//2]
    t2 = t[n//2:]
    t1.reverse() 
    t1 = t1 + t2 
    return t1 

if __name__ == '__main__':
    n = int(input())
    t = [int(x) for x in input().split()]
    print(*solve(n, t))
