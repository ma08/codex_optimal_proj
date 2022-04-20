
import sys

def solve(n, a, b):
    a, b = min(a, b), max(a, b) 
    if a == b:
        return n * a 
    else:
        if n % 2 == 0: 
            return (a * (n//2)) + (b * (n//2)) 
        else:
            return (a * (n//2)) + (b * (n//2)) + a 

q = int(input().strip())
for a0 in xrange(q):
    n, a, b = input().strip().split(' ')
    n, a, b = [int(n), int(a), int(b)] 
    print(solve(n, a, b))
