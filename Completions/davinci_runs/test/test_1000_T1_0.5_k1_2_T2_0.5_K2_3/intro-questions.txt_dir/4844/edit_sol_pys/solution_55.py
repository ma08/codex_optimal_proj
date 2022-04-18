import os


a = input()
b = input()
if os.path.exists(a) and os.path.exists(b):
    print("Файлы существуют")
    with open(a, 'r') as f:
        x = f.read()
    with open(b, 'r') as f:
        y = f.read()

for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, end=' ')

for i in range(N):
    for j in range(i+1, N):
        if m[i][j] == 0:
            a[i] = 0
            a[j] = 0
        else:
            a[i] = m[i][j]
            a[j] = m[i][j]

print(*a)
