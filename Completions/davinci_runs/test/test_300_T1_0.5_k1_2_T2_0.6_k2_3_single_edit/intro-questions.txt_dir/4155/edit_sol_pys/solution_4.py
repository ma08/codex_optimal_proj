

N = int(input())  # テストケースの数
h = list(map(int, input().split()))  # 各テストケースの値

cnt = 0  # カウンタ
for i in range(N):
    if h[i] > cnt:
        cnt = h[i]
print(cnt)
