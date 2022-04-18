# https://codeforces.com/contest/1352/problem/A

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if n < k:
        print(1)
    else:

# https://codeforces.com/contest/1352/problem/B
t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    while n:
        if n % 10 == 0:
            n /= 10
        else:
            n -= 1
            cnt += 1
    print(cnt)

# https://codeforces.com/contest/1352/problem/C
t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    if n == 2:
        print(x, y)
    else:
        print(x, x, y)
        print(n // k + n % k)
