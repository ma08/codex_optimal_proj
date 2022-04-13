n = int(input())
a = list(map(int, input().split()))

increasing = 0
decreasing = 1
res = [0 for _ in range(n)]
for i in range(n-1):
    if a[i] < a[i+1]:
        res[i] = increasing
    elif a[i] > a[i+1]:
        res[i] = decreasing
    else:
        print("NO")
        exit()
if a[0] > a[1]:
    res[0] = decreasing
if a[-1] < a[-2]:
    res[-1] = increasing
if res.count(0) == 0 or res.count(1) == 0:
    print("NO")
else:
    print("YES")
    print(*res)
