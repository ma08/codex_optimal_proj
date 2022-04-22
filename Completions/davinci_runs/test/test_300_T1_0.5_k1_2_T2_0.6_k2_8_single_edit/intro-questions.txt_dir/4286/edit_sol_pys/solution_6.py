
def main():
    n, m = map(int, input().split()) # nは頂点数、mは辺の数
    a = list(map(int, input().split())) # 各頂点にある果物の数
    g = [[] for _ in range(n + 1)] # 二次元配列を作成
    for _ in range(m):
        x, y, w = map(int, input().split()) # x, y, wを取得
        g[x].append((y, w)) # xからyまでのコストwの辺を作成
        g[y].append((x, w)) # yからxまでのコストwの辺を作成


    spt = [float('inf')] * (n + 1) # 最短距離の配列を生成
    spt[1] = 0 # 頂点１からの重みを0に設定
    q = [1] # 頂点１をキューに追加
    while q:
        u = q.pop(0) # キューから頂点を取り出す
        for v, w in g[u]: # uから伸びている頂点vについて見ていく
            if spt[v] > spt[u] + w: # vまでの最短距離が、uからvまでの重み+uまでの最短距離よりも大きかった場合
                spt[v] = spt[u] + w # vまでの最短距離を更新
                q.append(v) # 更新した頂点をキューに追加

    ans = sum(a)
    for i in range(2, n + 1):
        ans += min(spt[i], a[i - 1])

    print(ans)


if __name__ == '__main__':
    main()
