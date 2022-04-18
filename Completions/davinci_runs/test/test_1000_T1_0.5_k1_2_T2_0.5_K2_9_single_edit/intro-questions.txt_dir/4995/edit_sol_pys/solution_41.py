n = int(input())
a = []
b = []
for i in range(n):
    a.append(input())
    b.append(input())


for i in range(n):
    if a[i] == b[i]:
        print(a[i])
    else:
        print(a[i]+b[i])
