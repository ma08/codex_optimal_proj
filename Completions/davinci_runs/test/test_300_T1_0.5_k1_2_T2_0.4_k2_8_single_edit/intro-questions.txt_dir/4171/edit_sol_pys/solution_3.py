
n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = sum(a) // k

if sum(a) // k < 2:
    print(ans)
else:
    print(ans + sum(a) // k - 1)
