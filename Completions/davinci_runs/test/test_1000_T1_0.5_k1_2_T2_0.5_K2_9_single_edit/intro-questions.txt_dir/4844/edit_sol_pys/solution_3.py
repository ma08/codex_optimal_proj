
N = int(input())
m = []
for i in range(N):
    m.append(list(map(int, input().split())))

a = []
for i in range(N):
    a.append(0)

for i in range(N):
    a[i] = m[i][i+1]

print(*a)
