

n, k = list(map(int, input().split()))

if n % k == 0:
    print(0)
else:
    print(n % k)