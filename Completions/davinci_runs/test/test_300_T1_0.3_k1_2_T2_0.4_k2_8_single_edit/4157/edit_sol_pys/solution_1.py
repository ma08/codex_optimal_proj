
n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    if len(a) == 1:
        print(*a)
        break
    if len(a) == 2:
        if a[0] == a[1] // 2 or a[0] == a[1] * 3:
            print(*a)
            break
    if a[0] == a[1] // 2 or a[0] == a[1] * 3:
        a.pop(0)
    else:
        a.pop(0)
        a.pop(0)

