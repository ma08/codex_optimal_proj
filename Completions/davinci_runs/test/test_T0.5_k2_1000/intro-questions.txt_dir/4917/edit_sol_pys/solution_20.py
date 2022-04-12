

#cook your dish here
N = int(input())

def check(b):
    for i in range(N):
        if a[i]<=b<=b[i] and i!=N-1:
            return False
    return True

for _ in range(N):
    a,b = map(int,input().split())    
    if check(a) and check(b):
        print("Gunilla has a point")        
        break    
else:    
    print("Edward is right")    
