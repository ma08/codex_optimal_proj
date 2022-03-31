

# 問題文を整理すると、
# ある1つの100点問題を解いたとき、ボーナス1つによって得られる点は、
# 100点問題を解くのに必要な問題数+1より、1点少ないことが分かる。
# これを利用して、ボーナスを得るために必要な問題数を計算して、
# 最後に上限値を超えるまで問題数を増やしていく。
# この方針で解くと、解答が簡単に求まる。
# ただし、ボーナスを得るために必要な問題数が、ボーナス獲得点数より大きくなる場合がある。
# このときは、ボーナス獲得点数をそのまま加算して、ボーナスを得るために必要な問題数を計算する。
# これで解答が求まる。
# また、この方針だと、ボーナス獲得点数が大きい順にボーナスを得る必要があるので、
# それを考慮して、ボーナス獲得点数が大きい順にソートする。

# 入力
D, G = map(int, input().split())
problem_list = []
for i in range(D):
    p, c = map(int, input().split())
    problem_list.append([p, c])

# ボーナス獲得点数が大きい順にソート
problem_list.sort(key=lambda x:x[1], reverse=True)

# 合計点数
total_score = 0

# 問題数
count = 0

# 各ボーナスを得るために必要な問題数
for i in range(D):
    perfect_bonus_count = 0
    # 各ボーナスを得るために必要な問題数の計算
    if problem_list[i][1] != 0:
        perfect_bonus_count = ((i+1) * 100 * problem_list[i][0]) + problem_list[i][1]

    # ボーナスを得るために必要な問題数が、ボーナス獲得点数より大きい場合
    if perfect_bonus_count > problem_list[i][1]:
        # ボーナス獲得点数を加算
        total_score += problem_list[i][1]
        # 問題数を更新
        count += problem_list[i][0]
        # ボーナスを得るために必要な問題数を計算
        perfect_bonus_count = problem_list[i][1] / ((i+1) * 100)
        # 合計点数が、目標点数より大きい場合
        if total_score >= G:
            break
        # 合計点数が、目標点数より小さい場合
        else:
            # 問題数を更新
            count += int(perfect_bonus_count)
            # 合計点数を更新
            total_score += int(perfect_bonus_count) * ((i+1) * 100)
            # 合計点数が、目標点数より大きい場合
            if total_score >= G:
                break
    # ボーナスを得るために必要な問題数が、ボーナス獲得点数より小さい場合
    else:
        # 問題数を更新
        count += int(perfect_bonus_count)
        # 合計点数を更新
        total_score += int(perfect_bonus_count)
        # 合計点数が、目標点数より大きい場合
        if total_score >= G:
            break

print(count)