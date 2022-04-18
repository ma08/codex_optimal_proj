
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
b.sort()
c.sort()
s = 0
for i in range(n):
    for j in range(n):
        if b[i] > c[j]:
            s += 1
print(s)
