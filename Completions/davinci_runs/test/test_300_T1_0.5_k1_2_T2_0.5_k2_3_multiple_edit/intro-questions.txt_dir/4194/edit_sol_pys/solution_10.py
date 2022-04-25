
n, m = map(int, input().split())  # число полок и число книг
a = list(map(int, input().split()))  # количество страниц в книге

a.sort(reverse=True)

if a[-1] > n:
    print(-1)
    exit()

s = 0
for i in range(m):
    s += a[i]

print(n - s)
