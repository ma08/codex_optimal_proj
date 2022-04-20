

# N = int(input())
N = 127

# 出力値（最小操作数）
ans = float('inf')

# 6^nを計算する
for i in range(1, N+1):
    # 6^nを計算
    six = 6 ** i
    # 残り枚数を計算
    rest = N - six
    # 9^nを計算
    for j in range(1, rest+1):
        # 9^nを計算
        nine = 9 ** j
        # 残り枚数を計算
        rest = rest - nine
        # 残り枚数が0になったら、出力値を更新
        if rest == 0:
            ans = min(ans, i+j)
        # 残り枚数が負になったら、処理を終了
        elif rest < 0:
            break

print(ans)