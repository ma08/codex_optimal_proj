# coding: utf-8
# Your code here!


n = int(input())  # 山の数
h = list(map(int, input().split()))  # 山の高さ

if n == 1:  # 山が1つなら
    print('Yes')  # Yes
else:  # 山が2つ以上なら
    flag = True  # フラグを立てる
    for i in range(1, n):  # 2番目の山から最後の山まで
        if h[i] < h[i-1]:  # 前の山より小さいなら
            if h[i] < h[i-1] - 1:  # 前の山から1以上小さいなら
                flag = False  # フラグを倒す
                break  # ループを抜ける
            else:  # 前の山から1以下小さいなら
                h[i] = h[i-1]  # 前の山の高さに合わせる
    if flag:  # フラグが立っているなら
        print('Yes')  # Yes
    else:  # フラグが倒れているなら
        print('No')  # No
