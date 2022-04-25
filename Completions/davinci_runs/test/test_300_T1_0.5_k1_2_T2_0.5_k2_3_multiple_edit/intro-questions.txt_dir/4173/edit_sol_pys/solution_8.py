
q = int(input())

for i in range(q):
    n, a, b = [int(x) for x in input().split()]    
    print(n//2*min(a,b) + (n%2)*max(a,b))
