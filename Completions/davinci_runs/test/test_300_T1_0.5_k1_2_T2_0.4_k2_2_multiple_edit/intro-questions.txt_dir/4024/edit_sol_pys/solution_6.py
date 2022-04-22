

n, k = map(int, input().split())
s = input()
if k > n or k == 0:
    print(-1)
else:
    print(n - k + 1)
