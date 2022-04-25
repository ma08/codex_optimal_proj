n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        elif a[i][j] == 1:
            print('YES')
            exit()
print('NO')
