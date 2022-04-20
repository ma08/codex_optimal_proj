


def main():
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]
    x = list(map(int, input().split()))

    # 各アルゴリズムを完璧に理解するのに必要な本の数
    need = [0] * m
    for i in range(n):
        for j in range(m):
            if a[i][j] > 0:
                need[j] += 1

    # 各本の各アルゴリズムの理解度の合計
    total = [0] * m
    for i in range(n):
        for j in range(m):
            total[j] += a[i][j]

    # 各アルゴリズムについて、完璧に理解するのに必要な本の数を超えているかをチェック
    for i in range(m):
        if total[i] < x[i]:
            print(-1)
            return

    # 各アルゴリズムについて、完璧に理解するのに必要な本の数に達するまで、価格が最も低い本を買う
    ans = 0
    for i in range(m):
        cost = [0] * n
        for j in range(n):
            cost[j] = c[j] // a[j][i]
        index = cost.index(min(cost))
        ans += c[index]
        # 完璧に理解するのに必要な本の数に達するまで、価格が最も低い本を買う
        for j in range(need[i] - 1):
            c[index] += a[index][i]
            ans += c[index]
    print(ans)


if __name__ == '__main__':
    main()