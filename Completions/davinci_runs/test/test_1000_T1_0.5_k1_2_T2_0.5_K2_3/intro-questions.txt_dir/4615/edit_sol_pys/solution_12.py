

# A, B, C, D, E, F = map(int, input().split())
A, B, C, D, E, F = 1, 2, 10, 20, 15, 300

# 水の重さと砂糖の重さをそれぞれAからFまで実験する
# (水の重さ, 砂糖の重さ)のタプルのリストを作成
# 水の重さを100AからFまで、砂糖の重さをAからFまでとする
# それぞれの水の重さについて、砂糖の重さをAからFまで試していく
# このとき、砂糖の重さが水の重さより大きくなると、砂糖は溶けないのでbreakする
# また、水の重さがFを超える場合もbreakする
experiments = []
for w in range(A * 100, F + 1, A):
    for s in range(A, F + 1, A):
        if s > w:
            break
        if w + s > F:
            break
        experiments.append((w, s))

# 実験結果のうち、砂糖が溶けきっているものを抽出する
# 実験結果のうち、砂糖の重さがE倍以下の水の重さを抽出する
# また、砂糖の重さがAの場合は除外する
# 砂糖が溶けきっているもののうち、砂糖水の密度が最大のものを抽出する
# 砂糖水の密度は、砂糖の重さを水の重さ＋砂糖の重さで割った値とする
sugar_dissolved = [(w, s) for w, s in experiments if s <= w * E / 100]
sugar_dissolved = [(w, s) for w, s in sugar_dissolved if s > A]
if len(sugar_dissolved) > 0:
    sugar_dissolved = max(sugar_dissolved, key=lambda x: x[1] / (x[0] + x[1]))
    print(' '.join(map(str, sugar_dissolved)))
else:
    print('{} {}'.format(A * 100, 0))
