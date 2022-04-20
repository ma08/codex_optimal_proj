import sys
sys.setrecursionlimit(10**6)


def main():
    n, m = map(int, input().split())  # n:頂点数 m:辺の数
    a = list(map(int, input().split()))  # 各頂点のコスト
    g = [[] for _ in range(n + 1)]  # 隣接リスト
    for _ in range(m):  # 隣接リストを作成
        x, y, w = map(int, input().split())  # x:始点 y:終点 w:コスト
        g[x].append((y, w))  # 隣接リストに追加
        g[y].append((x, w))  # 隣接リストに追加

    spt = [float('inf')] * (n + 1)  # 最短経路木
    spt[1] = 0  # 最短経路木の初期化
    q = [1]  # 始点を追加
    while q:  # BFS
        u = q.pop(0)  # 一番左の要素を取り出す
        for v, w in g[u]:  # 始点uから伸びている先の頂点vとコストw
            if spt[v] > spt[u] + w:  # 最短経路木の更新
                spt[v] = spt[u] + w  # 最短経路木の更新
                q.append(v)  # 最短経路木の更新

    ans = sum(a)  # 全ての頂点を使う場合のコスト
    for i in range(2, n + 1):  # 最短経路木を使う場合のコスト
        ans += min(spt[i], a[i - 1])  # 最短経路木を使う場合のコスト

    print(ans)  # 答えの出力


if __name__ == '__main__':
    main()
