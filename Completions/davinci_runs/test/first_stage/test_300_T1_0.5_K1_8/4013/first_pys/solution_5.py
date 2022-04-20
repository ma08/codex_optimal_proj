

n = int(input())
a = input().split()
a = [int(x) for x in a]

a.sort()
print(min(a[n - 1] - a[1], a[n - 2] - a[0]))