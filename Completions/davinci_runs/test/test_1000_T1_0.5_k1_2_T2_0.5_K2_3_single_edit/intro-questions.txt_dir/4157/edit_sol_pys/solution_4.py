import sys
input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))

if n == 2:
    print(a[1], a[0], sep=' ')
elif n == 3:
    if a[0] * 3 == a[1] and a[1] * 2 == a[2]:
        print(a[0], a[1], a[2], sep=' ')
    else:
        print(a[2], a[0], a[1], sep=' ')
else:
    for i in range(n):
        if a[i] % 3 == 0:
            a[i] //= 3
        else:
            a[i] *= 2
    a.sort()
    print(*a)
