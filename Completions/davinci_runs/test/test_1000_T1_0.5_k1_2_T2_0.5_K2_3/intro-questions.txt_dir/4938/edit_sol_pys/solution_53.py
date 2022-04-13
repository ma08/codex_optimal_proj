

n = int(input())
l = list(map(int, input().split()))

x = int(input())

a = -1
b = -1
c = -1

for i in range(n-1):
    if l[i] == x:
        a = i
        break

for i in range(n - 1, -1):
    if l[i] == x:
        b = i
        break

if a == b:
    c = a + 1
else:
    c = b - a + 1

print(c)
