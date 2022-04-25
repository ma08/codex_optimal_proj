
# Solution1

n, k = map(int, input().split())
a = list(map(int, input().split()))

print(max(max(a) - min(a) - 2 * (k - 1), 0))
