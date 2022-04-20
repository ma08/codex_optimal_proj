
def main():
    n, m = map(int, input().split())  # n:頂点数 m:辺数
    edges = []  # 辺のリスト
    for i in range(m):  # 辺を入力
        u, v = map(int, input().split())  # u:始点 v:終点
        edges.append((u, v))  # 辺を追加
    print("YES")
    for i in range(m):  # 各辺について
        if edges[i][0] < edges[i][1]:
            print("0", end="")  # 0を出力
        else:
            print("1", end="")  # 1を出力


if __name__ == "__main__":
    main()
