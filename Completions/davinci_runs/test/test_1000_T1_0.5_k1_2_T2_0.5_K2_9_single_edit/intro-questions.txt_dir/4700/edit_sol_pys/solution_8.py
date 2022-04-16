
import sys

def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in range(m)]

    roads = [[] for _ in range(n)]  # 道路のリストを作成する
    for a, b in ab:
        roads[a-1].append(b-1)
        roads[b-1].append(a-1)

    max_h = [0 for _ in range(n)]  # 各観測所ごとに最高標高を求める
    for i in range(n):
        for j in roads[i]:
            if h[j] > max_h[i]:
                max_h[i] = h[j]

    ans = 0  # 各観測所からの最高標高を求める
    for i in range(n):
        if h[i] > max_h[i]:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
