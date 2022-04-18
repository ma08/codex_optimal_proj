import sys

n = [int(i) for i in input().split()]
k = int(input())

def fact(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

def ncr(n, r):
    return int(fact(n)/(fact(r)*fact(n-r)))

if k == 1:
    print(sum(n))
else:
    ans = 0
    for i in range(k):
        ans += n[i]*ncr(sum(n[i+1:]), k-i-1)
    print(ans)
