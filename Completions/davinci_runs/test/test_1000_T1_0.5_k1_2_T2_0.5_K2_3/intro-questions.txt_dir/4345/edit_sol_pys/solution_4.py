

n = int(input())
a = list(map(int, input().split()))

if len(a) == 1:
    print("YES")
    print(0)
else:
    increasing = 1
    decreasing = 0
    res = [0 for _ in range(n)]
    for i in range(n-1):
        if a[i] < a[i+1]:
            res[i] = increasing
        elif a[i] > a[i+1]:
            res[i] = decreasing
        else:
            print("NO")
            exit()
        if i == 0:
            if a[i] > a[i+1]:
                res[i] = decreasing
        if i == n-2:
            if a[i] < a[i+1]:
                res[i+1] = increasing
    if res.count(0) == 0 or res.count(1) == 0:
        print("NO")
    else:
        print("YES")
        print(*res)
