

a, b, k = map(int, input().split())
# a, b, k = 2, 3, 3
# a, b, k = 1000000000000, 1000000000000, 1000000000000 # TLE

a = max(0, a - k)
k -= min(k, a)
b = max(0, b - k)

print(a, b)
