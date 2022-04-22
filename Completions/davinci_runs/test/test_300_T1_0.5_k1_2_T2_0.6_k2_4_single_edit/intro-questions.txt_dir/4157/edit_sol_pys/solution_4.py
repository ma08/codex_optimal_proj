"""

n = int(input())
a = list(map(int, input().split()))

if n == 2:
    print(a[1], a[0])
elif n == 3:
    if a[0] * 3 == a[1] and a[1] * 2 == a[2]:
        print(a[0], a[1], a[2])
    else:
        print(a[2], a[0], a[1])
else:
    for i in range(n):
        if a[i] % 3 == 0:
            a[i] //= 3
        else:
            a[i] *= 2
    a.sort()
"""

n = int(input())
a = list(map(int, input().split()))

a.sort()

if n == 3:
    if a[0] * 3 == a[1] and a[1] * 2 == a[2]:
        print(*a)
    else:
        print(a[2], a[0], a[1])
else:
    for i in range(n):
        if a[i] % 3 == 0:
            a[i] //= 3
        else:
            a[i] *= 2
    print(*a)
    print(*a)
