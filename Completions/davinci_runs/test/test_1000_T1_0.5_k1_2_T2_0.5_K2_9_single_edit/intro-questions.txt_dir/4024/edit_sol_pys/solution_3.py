

n, k = map(int, input().split())
s = input()

if k > n or k == 0:
elif k == 1 and n == 1:
    print(0)
    print(-1)
else:
    print(n - k)
