
N = int(input())  # 整数の入力
h = list(map(int, input().split()))  # 整数の入力

cnt = 0
for i in range(N):
    if h[i] > cnt:
        cnt = h[i]
print(cnt)
