

# a, b, k = map(int, input().split())
# a -= min(a, k)
# k -= min(a+b, k)
# b -= min(b, k)
# print(a, b)

a, b, k = map(int, input().split())
a -= min(a, k)
k -= min(b, k)
b -= min(b, k)
print(a, b)
