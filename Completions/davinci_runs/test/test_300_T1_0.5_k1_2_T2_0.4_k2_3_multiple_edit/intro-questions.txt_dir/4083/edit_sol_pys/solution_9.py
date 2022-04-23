
n, k = map(int, input().split())
a = map(int, input().split())

print(max(a) - min(a) - k + 1)
