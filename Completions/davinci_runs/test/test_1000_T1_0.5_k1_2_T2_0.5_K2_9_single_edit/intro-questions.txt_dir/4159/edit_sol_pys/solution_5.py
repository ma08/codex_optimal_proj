
a,b,k = map(int, input().split())

if k <= a and k <= b:
    b -= k
elif k <= a and k > b:
    a -= k
    b = 0
elif k > a and k <= b:
    a = 0
    b -= k
    a -= k
else:
    a = 0
    b = 0

print(a,b)
