

n = int(input())
a = list(map(int, input().split()))

a.sort()

if a[0] == a[-1]:
    print(0)
elif a[0] + 1 == a[-1]:
    print(1)
elif a[0] + 2 == a[-1]:
    print(2)
else:
    print(-1)