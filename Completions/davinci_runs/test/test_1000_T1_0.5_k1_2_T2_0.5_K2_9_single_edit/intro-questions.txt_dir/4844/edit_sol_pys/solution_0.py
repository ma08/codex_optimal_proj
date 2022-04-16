

N = int(input())
a = []

m = []
for i in range(N):
    m.append(list(map(int, input().split())))

for i in range(N):
    for j in range(i+1, N):
        a.append(m[i][j])

print(*a)
