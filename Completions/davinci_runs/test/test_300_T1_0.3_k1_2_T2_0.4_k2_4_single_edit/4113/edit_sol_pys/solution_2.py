N = int(input())
a = [int(i) for i in input().split()]
a.sort()
if N % 2 == 0:
    print(a[N // 2] - a[N // 2 - 1])
else:
    print(0)

