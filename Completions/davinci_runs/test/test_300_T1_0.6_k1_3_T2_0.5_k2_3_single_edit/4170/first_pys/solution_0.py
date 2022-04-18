

n = int(input())
h = list(map(int, input().split()))

count = 0
c = 0
for i in range(n-1):
    if h[i] >= h[i+1]:
        c += 1
    else:
        if c > count:
            count = c
        c = 0

print(max(count, c))