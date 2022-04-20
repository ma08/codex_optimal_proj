
#
a, b, k = map(int, input().split())

while k > 0:
    if a > 0:
        a -= 1
    elif b > 0:
        b -= 1
    k -= 1

print(a, b)
