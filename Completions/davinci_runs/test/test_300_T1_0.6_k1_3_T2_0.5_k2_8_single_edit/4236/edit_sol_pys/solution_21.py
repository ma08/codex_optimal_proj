
n, m = map(int, input().split())  # количество процессов и количество ресурсов
a = []  # матрица авторизации
for i in range(n):
    a.append(list(map(int, input().split())))
c = []  # матрица текущего состояния
for i in range(n):
    c.append(list(map(int, input().split())))
r = []  # матрица запросов
for i in range(n):
    r.append(list(map(int, input().split())))
av = []  # вектор свободных ресурсов
for i in range(m):
    av.append(int(input()))
f = []  # вектор флагов
for i in range(n):
    f.append(0)
ans = []  # вектор ответа
for i in range(n):
    ans.append(0)
k = 0
while k < n:
    for i in range(n):
        if f[i] == 0:
            t = 0
            for j in range(m):
                if r[i][j] <= av[j]:
                    t += 1
            if t == m:
                for j in range(m):
                    av[j] += c[i][j]
                ans[i] = 1
                f[i] = 1
                k += 1
for i in ans:
    print(i, end=' ')
