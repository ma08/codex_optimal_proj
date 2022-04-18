

n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

a[0] = max(a[0] - b[1], 0)
b[1] = max(b[1] - a[0], 0)

a[2] = max(a[2] - b[0], 0)
b[0] = max(b[0] - a[2], 0)

a[1] = max(a[1] - b[2], 0)
b[2] = max(b[2] - a[1], 0)

print(min(a), max(a))
