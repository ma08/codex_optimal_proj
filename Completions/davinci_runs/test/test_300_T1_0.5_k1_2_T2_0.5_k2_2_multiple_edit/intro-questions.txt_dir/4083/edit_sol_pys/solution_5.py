
n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

if max(a) - min(a) - k >= 0:
    print(max(a) - min(a) - k)
else:
    print(0)
