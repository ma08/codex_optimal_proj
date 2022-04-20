
n = int(input())
a = list(map(int, input().split()))

#s = 0
s = a[0]
c = 0
for i in range(1, n):

    s += a[i]

    if s == 0:

        c += 1

        s = a[i]

print(c)
