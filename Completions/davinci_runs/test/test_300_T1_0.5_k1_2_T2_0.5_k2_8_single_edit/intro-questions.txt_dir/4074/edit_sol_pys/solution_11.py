
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(min(n, k - 1) + (n - 1) // (k - 1))
