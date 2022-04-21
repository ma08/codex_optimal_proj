

n,k = map(int,input().split())
a = list(map(int,input().split()))

if k == 1:
    print(0)
else:
    a.sort()
    sum_a = 0
    for i in range(n):
        sum_a += a[i]

    sum_b = 0
    for i in range(n-k):
        sum_b += a[i]

    print(sum_a-sum_b)
