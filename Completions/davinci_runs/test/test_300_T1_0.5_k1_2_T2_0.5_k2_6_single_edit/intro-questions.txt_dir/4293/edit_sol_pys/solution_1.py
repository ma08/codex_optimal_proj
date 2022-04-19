

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

c = []

for i in range(m):
    for j in range(n):
        if b[i] == a[j]:
            c.append(b[i])
            a[j] = -1
            break

c.sort()

for i in range(len(c)):
    print(c[i])
