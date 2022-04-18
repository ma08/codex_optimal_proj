

n = int(input()) # 数字を入力

ans = 0 # 答えを初期化
for i in range(1, n+1):
    num = len(str(i)) # 数字iを文字列に変換し、長さを取得
    if num % 2 != 0: # 偶数の場合
        ans += 1

print(ans) # 答えを出力
