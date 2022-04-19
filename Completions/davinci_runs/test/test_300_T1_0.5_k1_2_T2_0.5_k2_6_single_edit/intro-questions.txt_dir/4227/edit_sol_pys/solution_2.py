
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
MOD = 10 ** 9 + 7
N, M = map(int, input().split())  # N:頂点の数 M:辺の数
tree = [[] for _ in range(N)]  # 隣接リスト
for _ in range(M):  # 木を作る
    a, b = map(int, input().split())  # a, b:頂点
    tree[a - 1].append(b - 1)  # aの隣接リストにbを追加
    tree[b - 1].append(a - 1)  # bの隣接リストにaを追加
def dfs(v, visited):  # v:今いる頂点 visited:訪問済みの頂点
    visited.add(v)  # vを訪問済みにする
    for child in tree[v]:  # vの隣接頂点を調べる
        if child not in visited:  # 訪問済みでないなら
            dfs(child, visited)  # childに対して再帰
visited = set()  # 訪問済みの頂点の集合
dfs(0, visited)  # 0から再帰
if len(visited) != N:  # 訪問済みの頂点の数がNと一致しないなら
    print(0)  # 分岐数は0
    sys.exit()  # 終了
ans = 1  # 分岐数
for i in range(N):  # 各頂点について
    if i == 0:  # iが0なら
        continue  # スキップ
    if len(tree[i]) > 1:  # iの隣接頂点の数が2以上なら
        ans *= len(tree[i])  # 分岐数にiの隣接頂点の数を掛ける
        ans %= MOD  # ansをMODで割った余りをansに入れる
print(ans)  # 分岐数を出力
