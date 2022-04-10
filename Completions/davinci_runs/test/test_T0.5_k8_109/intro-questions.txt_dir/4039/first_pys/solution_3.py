

n, r = map(int, input().split())
a = []
b = []
for i in range(n):
    a_i, b_i = map(int, input().split())
    a.append(a_i)
    b.append(b_i)

a.sort()
b.sort()

if (a[0] > r):
    print("NO")
else:
    r += b[-1]
    if (r < 0):
        print("NO")
    else:
        print("YES")