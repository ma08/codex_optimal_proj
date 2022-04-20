
a, b, k = map(int, input().split())
c = min(a, k)
a -= c
k -= c
b = max(0, b - k)
print(a, b)
