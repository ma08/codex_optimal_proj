

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

if m > sum(a):
    print(-1)
else:
    days = 0
    for i in range(n):
        if a[i] > days:
            days += 1
    print(days)