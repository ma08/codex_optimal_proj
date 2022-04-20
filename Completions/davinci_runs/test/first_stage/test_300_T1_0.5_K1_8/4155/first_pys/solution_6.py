

N = int(input())
h = list(map(int, input().split()))

cnt = 0
for i in range(1, N + 1):
    if h[i - 1] > cnt:
        cnt = h[i - 1]
    if h[i - 1] >= cnt:
        cnt += 1
print(cnt)