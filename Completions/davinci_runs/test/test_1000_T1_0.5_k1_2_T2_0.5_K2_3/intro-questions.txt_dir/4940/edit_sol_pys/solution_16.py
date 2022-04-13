
# 연산자 끼워넣기
n, m = map(int, input().split())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))

t = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        t[i][j] = max(t[i - 1][j - 1] + p[i - 1][j - 1], t[i][j - 1])

print(" ".join(map(str, t)))
