N = int(input())
h = list(map(int,input().split()))

count = 0
for i in range(N):
    if h[i] > count:
        count = h[i]
print(count)
