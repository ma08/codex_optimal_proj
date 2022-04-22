
n = int(input())
h = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if h[i] > cnt:
        cnt = h[i]
print(cnt)
