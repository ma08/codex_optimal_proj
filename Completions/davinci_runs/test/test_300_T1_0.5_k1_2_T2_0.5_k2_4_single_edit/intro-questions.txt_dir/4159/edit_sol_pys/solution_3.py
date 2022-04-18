a, b, k = map(int, input().split())


if k > a:
    k -= a
    a = 0
if k > b:
    b = 0
a -= k
b -= k

print(a,b)
