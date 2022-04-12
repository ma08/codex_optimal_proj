
import sys

def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in range(m)]

    # 道路のリストを作成する
    roads = [[] for _ in range(n)]
    for a, b in ab:
        roads[a-1].append(b-1)
        roads[b-1].append(a-1)

    # 各観測所ごとに最低標高を求める
    min_h = [10**10 for _ in range(n)]
    for i in range(n):
        for j in roads[i]:
            if h[j] <= min_h[i]:
                min_h[i] = h[j]

    # 各観測所からの最低標高を求める
    ans = 0
    for i in range(n):
        if h[i] > min_h[i]:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
