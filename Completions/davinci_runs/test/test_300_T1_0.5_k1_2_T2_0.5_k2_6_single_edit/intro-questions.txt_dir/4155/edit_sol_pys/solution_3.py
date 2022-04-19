

n = int(input())  # 入力
h = list(map(int, input().split()))  # 入力

ans = 0  # 初期化
for i in range(n):
    if h[i] > 0:  # 判定
        ans += 1  # 加算
        for j in range(i+1, n):  # 繰り返し
            if h[j] > 0:  # 判定
                h[j] -= 1  # 減算

print(ans)  # 出力
