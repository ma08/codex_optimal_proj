# Количество денег в виде долларов в первой строке

n, m = map(int, input().split())

first_line = []
for _ in range(n):
    first_line.append(input())

count = 0
for i in range(m):
    if first_line[0][i] == '$':
        count += 1
        while i < m and first_line[0][i] == '$':
            i += 1

print(count)
