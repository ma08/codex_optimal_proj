n, p = map(int, input().split())
a = list(map(int, input().split()))
if sum(a) > p or sum(a) < -p or sum(a) + p < 0 or sum(a) - p > 0:
    print(0)    
else:    
    print(p - abs(sum(a)))
