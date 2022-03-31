n, k = map(int, input().split())
s = input()

if k <= n:
    print(n - k)
else:
    if k % n == 0:
        print(-1)
    else:
        print(n - k % n)
