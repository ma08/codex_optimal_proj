
n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

if max(a) - min(a) - k + 1 < 0:
    print(0)
else:
    print(max(a) - min(a) - k + 1)
