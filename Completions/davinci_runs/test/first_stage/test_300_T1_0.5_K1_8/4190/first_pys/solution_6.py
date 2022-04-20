

def get_min_c_array(a,b):
    n = len(a)
    c = [0] * n
    for i in range(n):
        c[(a[i]+b[i])%n] += 1
    for i in range(1,n):
        c[i] += c[i-1]
    for i in range(n-1,-1,-1):
        c[i] = c[i-1] if i > 0 else 0
    for i in range(n):
        c[(a[i]+b[i])%n] += 1
    return c

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(*get_min_c_array(a,b))