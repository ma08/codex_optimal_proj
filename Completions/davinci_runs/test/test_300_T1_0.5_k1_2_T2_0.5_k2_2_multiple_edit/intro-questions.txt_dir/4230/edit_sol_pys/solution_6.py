n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

if x <= a[0]:
    print(a[0]-x)
elif x >= a[-1]:
    print(x-a[-1])
else:
    for i in range(1, n):
        if x <= a[i]:
            print(min(x-a[i-1], a[i]-x))
            break
