
n = [int(i) for i in input().split()] # input list of numbers
k = int(input()) # input k

def fact(num):
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
    for i in range(1, k+1):
        ans += n[i-1]*ncr(sum(n[i:]), k-i)
    print(ans)
