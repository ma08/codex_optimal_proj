n, k = map(int, input().split())
a = [int(i) for i in input().split()]

def fact(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans

def ncr(n, r):
    return int(fact(n) / (fact(r) * fact(n - r)))

if k == 1:
    print(sum(a))
else:
    ans = 0
    for i in range(1, k + 1):
        ans += a[i - 1] * ncr(sum(a[i:]), k - i)
    print(ans)
