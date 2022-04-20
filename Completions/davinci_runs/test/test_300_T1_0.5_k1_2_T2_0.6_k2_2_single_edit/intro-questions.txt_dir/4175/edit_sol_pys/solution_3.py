

import sys
 
 
N = int(input())  # 行数
words = []  # 文字列リスト
 
for i in range(N):  # 行数分入力を受け付ける
    words.append(input())  # 追加
 
for i in range(N):  # 行数分繰り返す
    if i == 0:  # 最初の文字列はどれでも良いのでスルー
        pass  # 何もしない
    else:  # それ以外
        if words[i] in words[:i] or words[i][0] != words[i-1][-1]:  # 今までの配列に同じものがあるか、先頭と末尾が一致しない
            print('No')  # No
            sys.exit()  # 終了
 
print('Yes')  # Yes
