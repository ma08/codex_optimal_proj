
n, w = map(int, input().split())
a = list(map(int, input().split()))

i = 0
j = 0

for i in range(n):
    if a[i] > w or a[i] < 0:
        j = w+1
        break;
    j += a[i]
    if j > w:
        break;

if i == n-1:
    print(w-j+1)
