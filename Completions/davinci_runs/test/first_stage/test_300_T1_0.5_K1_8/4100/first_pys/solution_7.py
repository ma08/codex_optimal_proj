

n, k, q = map(int, input().split())
A = []
for i in range(q):
    a = int(input())
    A.append(a)

points = [k] * n
for a in A:
    points[a - 1] += 1
    for i in range(n):
        if i != a - 1:
            points[i] -= 1

for i in range(n):
    if points[i] <= 0:
        print("No")
    else:
        print("Yes")