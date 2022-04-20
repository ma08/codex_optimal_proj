

# SOLUTION
n, m = map(int, input().split())
a = [0] * (m+1)
for i in range(n):
    l, r = map(int, input().split())
    for j in range(l, r+1):
        a[j] = 1

print(m - sum(a))
for i in range(1, m+1):
    if a[i] == 0:
        print(i, end=' ')