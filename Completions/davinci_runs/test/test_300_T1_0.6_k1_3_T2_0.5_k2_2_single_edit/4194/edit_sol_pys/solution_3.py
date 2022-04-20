
N, M = map(int, raw_input().split())
A = map(int, raw_input().split())

# 入力は昇順にソートしておく
A = sorted(A)

# 各作業について終わるまでの日数を合計する
# その結果、最大値がN以下であれば、それを出力する
# そうでなければ、答えは-1である
val = sum(A)
if val <= N:
    print(N - val)
else:
    print(-1)
