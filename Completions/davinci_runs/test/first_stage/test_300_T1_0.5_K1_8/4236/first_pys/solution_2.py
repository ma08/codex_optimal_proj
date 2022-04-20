

n, m = map(int, input().split())

points = [1] * (m+1)

for i in range(n):
    l, r = map(int, input().split())
    for j in range(l, r+1):
        points[j] = 0

print(sum(points))
for i in range(len(points)):
    if points[i]:
        print(i, end=' ')
print()