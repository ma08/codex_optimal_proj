

A, B, C, D, E, F = map(int, input().split())  # A:水の初期量 B:砂糖の初期量 C:砂糖水の初期量 D:水の消費量 E:砂糖水の消費量 F:合計量

experiments = []
for w in range(0, F + 1, 100 * A):
    for s in range(0, F + 1, B):
        if s > w or w + s > F:
            break
        experiments.append((w, s))  # (水の重さ, 砂糖の重さ)のタプルのリストを作成

sugar_dissolved = [(w, s) for w, s in experiments if s <= w * E // 100]  # 砂糖が溶けきっているものを抽出する
sugar_dissolved = [(w, s) for w, s in sugar_dissolved if s > 0]  # 砂糖の重さが0の場合は除外する
if len(sugar_dissolved) > 0:
    sugar_dissolved = max(sugar_dissolved, key=lambda x: x[1] / (x[0] + x[1]))  # 砂糖水の密度が最大のものを抽出する
    print(' '.join(map(str, sugar_dissolved)))
else:
    print('0 0')
