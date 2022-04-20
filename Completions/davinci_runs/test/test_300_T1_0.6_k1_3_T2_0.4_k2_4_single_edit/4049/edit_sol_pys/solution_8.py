
n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

a[0] = max(0, a[0] - b[1])
b[1] = max(0, b[1] - a[0])
a[2] = max(0, a[2] - b[0])
b[0] = max(0, b[0] - a[2])
a[1] = max(0, a[1] - b[2])
b[2] = max(0, b[2] - a[1])

print(min(a), max(a))
