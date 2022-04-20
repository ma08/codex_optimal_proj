

n, k = map(int, input().split())
a = list(map(int, input().split()))

m = min(a)
M = max(a)

if M-m+1 < k:
    print(-1)
else:
    print(M-m-k+1)