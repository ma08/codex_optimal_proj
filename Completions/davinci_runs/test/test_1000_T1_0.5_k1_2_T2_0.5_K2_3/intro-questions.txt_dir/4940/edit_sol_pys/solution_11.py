
def main():
    n, m = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(n)]  # 読み込み
    t = [0] * n  # 各列の最大値を入れるリスト
    for j in range(m):
        for i in range(n):
            if t[i] < max(t):
                t[i] = max(t)
            t[i] += p[i][j]
    print(*t)

if __name__ == '__main__':
    main()
