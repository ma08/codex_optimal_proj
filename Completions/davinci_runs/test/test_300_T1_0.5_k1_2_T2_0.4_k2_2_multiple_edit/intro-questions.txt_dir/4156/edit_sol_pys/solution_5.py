
n, w = map(int, input().split())
a = list(map(int, input().split()))

i = 0
j = 0

for i in range(n):
    if a[i] > w or a[i] < -w: # check if the value is in the range
        print(0)
        break
    j += a[i]
    if j > w or j < -w: # check if the sum is in the range
        print(0)
        break

if i == n-1:
    print(w-j+1)
