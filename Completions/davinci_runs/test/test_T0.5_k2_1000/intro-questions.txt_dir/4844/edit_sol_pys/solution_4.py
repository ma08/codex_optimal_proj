N = int(input())
M = []
for i in range(N):
    M.append(list(map(int, input().split())))

a = []
for i in range(N):
    a.append(1)

for i in range(N):
    for j in range(N):
        if M[i][j] == 0:
            a[i] = 1
            a[j] = 1

print(*a)
