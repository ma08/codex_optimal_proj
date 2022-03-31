

n, k = map(int, input().split())
s = input()

if k > n*(n+1)//2:
    print(-1)
else:
    cost = 0
    for i in range(n):
        if k <= n-i:
            cost += (n-i)*(n-i+1)//2 - k
            break
        else:
            k -= n-i
            cost += n-i
    print(cost)