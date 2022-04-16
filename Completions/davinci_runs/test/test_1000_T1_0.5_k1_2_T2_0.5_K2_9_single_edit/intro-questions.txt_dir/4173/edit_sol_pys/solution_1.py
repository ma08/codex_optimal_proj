
import sys
q = int(input())

for i in range(q):
    n, a, b = [int(x) for x in sys.stdin.readline().split()]
    
    min_bottles = n//2
    min_cost = min_bottles * b + (n%2)*a
    if a > b:
        min_cost = min(min_cost, (n//2)*a + (n%2)*b)
    
    sys.stdout.write(str(min_cost))
