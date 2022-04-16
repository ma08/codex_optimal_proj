
n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

print(max(0, max(a) - min(a) - k + 1))
