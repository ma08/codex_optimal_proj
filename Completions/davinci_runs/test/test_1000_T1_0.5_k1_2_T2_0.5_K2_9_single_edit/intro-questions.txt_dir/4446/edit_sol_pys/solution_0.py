
a, b, c, k = map(int, input().split())
ans = min(a, k)
k -= ans
if k > 0:
    ans -= min(b, k)
print(ans)
