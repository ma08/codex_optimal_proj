
n = int(input())
h = list(map(int, input().split()))
count = 0
for i in range(1,n):
    if h[i-1] >= h[i]:
        count += 1
    else:
        h[i] -= 1
print(count)
