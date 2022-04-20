
n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

min_a = min(a)
max_a = max(a)
print(max(max_a - min_a, (max_a - 1) - (min_a + k - 1)))
