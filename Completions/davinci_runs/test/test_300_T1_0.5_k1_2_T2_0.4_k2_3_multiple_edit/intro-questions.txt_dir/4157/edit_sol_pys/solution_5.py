

n = int(input())
a = list(map(int, input().split()))
a.sort()
if n == 2:
    print(a[1], a[0])
elif n == 3:
    if a[0] * 3 == a[1] and a[1] * 2 == a[2]:
        print(a[0], a[1], a[2])
    else:
        print(a[2], a[0], a[1])
else:
    for i in range(1, n):
        if a[i] % a[0] == 0:
            a[i] //= a[0]
        elif a[0] % a[i] == 0:
            a[0] //= a[i]

    print(*a)
