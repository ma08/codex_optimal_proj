import sys
sys.setrecursionlimit(10**7)


    # スペース区切り整数の入力
def main():
    n = int(input())
    x = list(map(int, input().split()))

    # スタート地点
    s = int(input())

    # グラフ
    graph = [[] for _ in range(n)]
    for i, xi in enumerate(x):
        graph[i].append(xi)

    # 各頂点の訪問状態
    seen = [False] * n

            if i == 0:
                max_p += len(idx) - 1
            elif i == n:
                max_p += len(idx) - 1
            else:
                max_p += len(idx)

    print(min_p, max_p)


if __name__ == '__main__':
    main()
