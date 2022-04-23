

n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

print(min(a[0] - b[1], a[2] - b[0], a[1] - b[2]), max(a[0] - b[1], a[2] - b[0], a[1] - b[2]))
