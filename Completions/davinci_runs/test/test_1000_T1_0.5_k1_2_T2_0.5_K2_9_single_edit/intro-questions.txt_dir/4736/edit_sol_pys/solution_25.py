
def fact(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

def ncr(n, k):
    return int(fact(n)/(fact(k)*fact(n-k)))

n, k = [int(i) for i in input().split()]

ans = 0
for i in range(1, k+1):
    ans += i*ncr(n+1, i)
print(ans)
