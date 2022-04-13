
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

a.sort()

s1 = 0
s2 = 0
for i in range(len(a)):
    if i < len(a) / 2:
        s1 += a[i] ** 2
    else:
        s2 += a[i]

print(s1 * s2)
