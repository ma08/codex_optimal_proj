

n, w = map(int, input().split())
a = list(map(int, input().split()))

i = 0
j = 0

for i in range(n):
    if a[i] > w or a[i] < -w:
        print(0)
        break
    j += a[i]
    if j > w:
        break
    if j < 0:
        print(1)
        print(0)
        break

if i == n-1:
    if j < 0:
        print(0)
    else:
        print(w-j+1)
