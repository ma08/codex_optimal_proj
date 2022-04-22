

N = int(input())  # 入力
S = list(input())  # 入力

# 赤、白、青の数をカウントする
r_count = 0
w_count = 0
b_count = 0
for i in range(N):  # Sの要素数だけ繰り返す
    if S[i] == 'R':
        r_count += 1
    elif S[i] == 'W':
        w_count += 1
    else:
        b_count += 1

# 赤、白、青をそれぞれの文字数だけ繰り返す
r_list = ['R']*r_count
w_list = ['W']*w_count
b_list = ['B']*b_count

ans = 0
for r in range(r_count+1):
    for w in range(w_count+1):
        # 赤、白、青の数を求める
        r_num = r
        w_num = w
        b_num = N-r-w

        # 赤、白、青をそれぞれの文字数だけ繰り返したリストの中から
        # 赤、白、青の数を抽出する
        r_list_sub = r_list[:r_num]
        w_list_sub = w_list[:w_num]
        b_list_sub = b_list[:b_num]

        # 赤、白、青をそれぞれの文字数だけ繰り返したリストの中から
        # 赤、白、青の数を抽出したものを結合していく
        sub_list = r_list_sub + w_list_sub + b_list_sub

        # 赤、白、青をそれぞれの文字数だけ繰り返したリストの中から
        # 赤、白、青の数を抽出していく
        sub_list_2 = [r_list[r_num]] + [w_list[w_num]] + [b_list[b_num]]

        # 赤、白、青をそれぞれの文字数だけ繰り返したリストの中から
        # 赤、白、青の数を抽出していく
        sub_list_3 = r_list[r_num+1:] + w_list[w_num+1:] + b_list[b_num+1:]

        # 赤、白、青をそれぞれの文字数だけ繰り返したリストの中から
        # 赤、白、青の数を抽出したものを結合していく
        sub_list_4 = sub_list + sub_list_2 + sub_list_3

        # 一致しているかどうかを判定
        if sub_list_4 == S:
            ans += 1

print(ans)
