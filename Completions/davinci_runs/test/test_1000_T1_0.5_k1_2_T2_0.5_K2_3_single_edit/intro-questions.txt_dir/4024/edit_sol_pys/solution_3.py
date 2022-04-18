

n, k = map(int, input().split())
s = input()

if k > n or k == 0:
    print(0)
else:
    print(n - k + 1)
