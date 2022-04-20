

def main():
    n, m, d = map(int, input().split())  # n: 頂点数, m: 辺数, d: 最大距離
    edges = [tuple(map(int, input().split())) for _ in range(m)]  # edges: 辺のリスト
    # d == 0 の場合

    if d == 0:
    # d == n-1 の場合
        print('YES')
        for i in range(2, n+1):
            print(1, i)
    elif d == n-1:
        print('YES')
        for i in range(2, n+1):
            print(i-1, i)
    else:
        print('NO')

if __name__ == '__main__':
    main()
