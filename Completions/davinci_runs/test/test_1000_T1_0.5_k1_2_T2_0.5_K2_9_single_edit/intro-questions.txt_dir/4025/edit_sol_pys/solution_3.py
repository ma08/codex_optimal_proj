

def f(n):
    return n*(n+1)//2

n, k = [int(x) for x in input().split()]

if k == 1:
    print(f(n-1))
    exit()

ans = 0

for i in range(1, n+1):
    if i >= k:
        ans += f(n//i)

print(ans)
