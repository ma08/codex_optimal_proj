
n, w = map(int, input().split())
a = list(map(int, input().split()))

i = 0
j = 0

while i < n:
    if a[i] > w or a[i] < -w:
        print(0)
        break
    j += a[i]
    if j > w or j < -w:
        print(0)
    i += 1
        break

if j >= 0 and j <= w:
    print(w - j + 1)
