

# SOLUTION
q = int(input())

for i in range(q):
    n, a, b = map(int, input().split())
    
    if (n % 2 == 0):
        print(a * (n//2))
    else:
        print(min(a * (n//2) + b, a * (n//2 + 1)))