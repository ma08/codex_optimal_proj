
n, k = map(int, input().split())
s = input()

if k > n or k == 0:
    print(-1)
elif k == 1:
    print(0)
elif n == k:
    print(n - 1)
else:  # k < n
    print(n - k)
