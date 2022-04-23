
n, w = map(int, input().split())
a = list(map(int, input().split()))
j = a[0]

for i in range(n):
    j += a[i]
    if j > w or j < -w or a[i] > w or a[i] < -w:
        print(0)
        break

if i == n-1:
    print(w-j+1)
