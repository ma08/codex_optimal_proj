

n, k, m = map(int, input().split())
a = list(map(int, input().split()))

sum_a = sum(a)

if n*m > sum_a:
    print(n*m - sum_a)
elif n*m == sum_a:
    print(0)
else:
    print(-1)