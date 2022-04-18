

N = int(input())  # 標準入力

count = 0  # カウント用変数

for i in range(1, N+1):
    count += len(str(i)) % 2  # iを文字列に変換して長さを取得し、その偶奇を判定。奇数なら1, 偶数なら0になる

print(count)  # 答えを出力
