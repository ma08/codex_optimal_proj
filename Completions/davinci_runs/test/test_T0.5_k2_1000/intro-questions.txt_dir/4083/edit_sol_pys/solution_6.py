
n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

print(max(a) - min(a) - k + 1 if max(a) - min(a) - k + 1 > 0 else 0)
