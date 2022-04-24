
n, k = map(int, input().split())
a = list(map(int, input().split()))
if n == 1:
    print("YES")
    print(1)
else:
    b = [0]*n
    for i in range(n):
        if a[i] == a[0]:
            b[i] = 1
        else:
            b[i] = 2
    if a[0] in a[1:]:
        print("NO")
    else:
        print("YES")
        print(*b)

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
d = [10,11,12]

for i in range(0, len(a)):
    print(a[i], end=' ')
    print(b[i], end=' ')
    print(c[i], end=' ')
    print(d[i], end=' ')
    print()
