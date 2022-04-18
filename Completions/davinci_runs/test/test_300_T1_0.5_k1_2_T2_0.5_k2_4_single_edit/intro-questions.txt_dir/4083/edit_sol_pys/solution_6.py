

n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

print(max(a) - min(a) - 2 * k + 1)
