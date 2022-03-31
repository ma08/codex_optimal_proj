

n = int(input())
a = [input() for _ in range(n)]

d = {}
for i in range(n):
    d[a[i]] = d.get(a[i], 0) + 1

if len(d) == 1:
    print("YES")
    for i in range(n):
        print(a[i])
else:
    print("NO")