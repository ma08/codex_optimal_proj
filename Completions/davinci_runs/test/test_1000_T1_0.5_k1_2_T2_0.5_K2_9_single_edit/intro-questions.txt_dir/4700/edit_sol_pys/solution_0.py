
# import sys

def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in range(m)]

    # 各観測所からの最高標高を求める
    # 標高を求めるために、観測所ごとに最高標高を求める
    # 各観測所ごとに最高標高を求めるために、道路のリストを作成する
    # 道路のリストを作成するために、道路の情報を使用する
    # 道路の情報から、道路のリストを作成する
    # 各観測所ごとに最高標高を求める
    # 各観測所からの最高標高を求める

    # 道路のリストを作成する
    roads = [[] for _ in range(n)]
    for a, b in ab:
        roads[a-1].append(b-1)
        roads[b-1].append(a-1)

    # 各観測所ごとに最高標高を求める
    max_h = [0 for _ in range(n)]
    for i in range(n):
        for j in roads[i]:
            if h[j] > max_h[i]:
                max_h[i] = h[j]

    # 各観測所からの最高標高を求める
    ans = 0
    for i in range(n):
        if h[i] > max_h[i]:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
