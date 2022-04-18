

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

k = int(input())

for i in range(n):
    for j in range(m):
        if a[i][j] == k:
            print(i + 1, j + 1)
            exit()

print("0 0")
