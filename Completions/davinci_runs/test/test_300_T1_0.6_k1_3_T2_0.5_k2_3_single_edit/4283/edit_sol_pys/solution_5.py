

n = int(input())
a = [int(i) for i in input().split()]
a = sorted(a)
print(min(a[n - 1] - a[0], 5))
