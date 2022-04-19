
n = int(input())  # 行数
s = input()  # 入力
count = 1  # 初期化
for i in range(1, n):  # 1からn-1まで
    if s[i] != s[i-1]:  # 隣り合う文字が異なるなら
        count += 1  # 数を増やす
print(count)  # 出力
