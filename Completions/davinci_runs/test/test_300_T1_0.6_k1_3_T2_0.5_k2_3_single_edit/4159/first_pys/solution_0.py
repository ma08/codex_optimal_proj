

# a, b, k = map(int, input().split())
# a -= min(a, k)
# k -= min(a+b, k)
# b -= min(b, k)
# print(a, b)

a, b, k = map(int, input().split())
a = max(a - k, 0)
k -= min(a+b, k)
b = max(b - k, 0)
print(a, b)