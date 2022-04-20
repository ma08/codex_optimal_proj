

#===main===
d, g = map(int, input().split())
p = []
c = []
for i in range(d):
    pi, ci = map(int, input().split())
    p.append(pi)
    c.append(ci)

# 全てのコースを初期化
course = []
for i in range(d):
    course.append([i+1, p[i], c[i]])

# 全てのコースで問題を解いた場合の満点・合計点数
full_score = 0
full_total = 0
for i in range(d):
    full_score += course[i][1] * course[i][0] * 100
    full_total += course[i][1] * course[i][0] * 100 + course[i][2]

# 全てのコースで問題を解いた場合の満点・合計点数が目標値以上の場合は全て解く
if full_total >= g:
    print(full_score)
    exit()

# 全てのコースで問題を解いた場合の満点・合計点数が目標値未満である場合
# 全てのコースを解いた後、目標値に近いコースから必要な問題数を加算していく
else:
    # 全てのコースを解く
    ans = full_score

    # コースを降順にソート
    course.sort(key=lambda x: x[2], reverse=True)

    # 目標値に近いコースから必要な問題数を加算していく
    for i in range(d):
        # 目標値を超える場合は終了
        if ans >= g:
            break
        # 目標値に近いコースから必要な問題数を加算していく
        else:
            # 完全ボーナスを超える場合はボーナス分を加算し、残りはコース単位で加算
            if ans + course[i][2] >= g:
                ans += g - ans
            # 完全ボーナスを超えない場合は完全ボーナス分を加算し、残りはコース単位で加算
            else:
                ans += course[i][2]
                # コース単位で加算
                for j in range(course[i][1]):
                    # 目標値を超える場合は終了
                    if ans >= g:
                        break
                    # 目標値に近いコースから必要な問題数を加算していく
                    else:
                        ans += course[i][0] * 100

    # 必要な問題数を出力
    print(ans)