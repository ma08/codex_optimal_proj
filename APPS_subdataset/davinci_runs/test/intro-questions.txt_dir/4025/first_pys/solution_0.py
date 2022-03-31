

a, b, c = [int(x) for x in input().split()]

res = 0
res += min(a, b, c)
res += min(a, b) + min(a, c) + min(b, c)
res += min(a, b) + min(a, c) + min(b, c)

print(res)