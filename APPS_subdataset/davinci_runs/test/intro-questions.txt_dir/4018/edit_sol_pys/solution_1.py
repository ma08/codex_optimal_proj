n, k = map(int, input().split())
s = input()

print(n - k if k <= n else -1 if k % n == 0 else n - k % n)
