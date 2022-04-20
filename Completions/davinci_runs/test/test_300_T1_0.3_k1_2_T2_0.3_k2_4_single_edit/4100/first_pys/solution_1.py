

n, k, q = map(int, input().split())
a = [int(input()) for _ in range(q)]

p = [k] * n
for i in range(q):
    for j in range(n):
        if j != a[i] - 1:
            p[j] -= 1

for i in range(n):
    if p[i] > 0:
        print("Yes")
    else:
        print("No")