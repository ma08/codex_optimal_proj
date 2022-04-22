
n, k = map(int, input().split())
a = list(map(int, input().split()))

print(max(a) - min(a) if max(a) - min(a) > k else 0)
