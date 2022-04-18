# coding: utf-8

n = int(input()) # 整数の入力
a = list(map(int, input().split())) # スペース区切りの整数の入力
a.sort() # 昇順にソート
count = 1 # 1番目の数字は必ず答えに含むので1
for i in range(1, n): # 1番目の数字は既にカウントしているので2番目からn番目まで
    if a[i] != a[i-1]: # 前の数字と同じでないならば
        count += 1 # カウントを１増やす
print(count) # カウント数を出力
