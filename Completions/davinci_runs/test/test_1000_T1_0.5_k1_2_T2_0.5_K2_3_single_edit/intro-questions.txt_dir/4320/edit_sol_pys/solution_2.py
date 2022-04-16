

t = int(input())

for i in range(t):
    n = int(input())
    s = 0
    j = 1
    while s < n:
        s += j
        j *= 2
    print(n//(j//2)) 
    
