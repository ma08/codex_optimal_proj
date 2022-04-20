
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

s = 0
for i in range(n):
    s += b[a[i] - 1]
    if i != n - 1:
        if a[i] == a[i + 1] - 1:
            s += c[a[i] - 1]

print(s)
