

a, b, k = map(int, input().split())
# a, b, k = 2, 3, 3

k -= min(a, k)
a -= min(a, k)
b -= min(b, k)

print(a, b)
