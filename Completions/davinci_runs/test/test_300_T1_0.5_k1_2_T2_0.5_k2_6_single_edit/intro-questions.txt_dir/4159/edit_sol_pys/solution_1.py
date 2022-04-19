
k -= min(a,k)
a,b,k = map(int, input().split())

if k <= a:
    a -= k
else:
    b -= min(b,k)

print(a,b)
