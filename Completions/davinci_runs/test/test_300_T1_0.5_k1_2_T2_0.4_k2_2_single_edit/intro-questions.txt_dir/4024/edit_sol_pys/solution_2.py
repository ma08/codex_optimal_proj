
n, k = map(int, input().split())  # n = 3, k = 3

if k > n or k == 0:
    print(-1)

print(n - k)
