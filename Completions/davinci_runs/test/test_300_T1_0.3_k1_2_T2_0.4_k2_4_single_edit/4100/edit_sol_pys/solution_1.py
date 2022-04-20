
n, k, q = map(int, input().split())
a = [int(input()) for _ in range(q)]

p = [k] * n
for i in range(q):
    p[a[i] - 1] += 1

for i in range(n):
    if p[i] > 0:
        print("Yes")
    else:
        print("No")
