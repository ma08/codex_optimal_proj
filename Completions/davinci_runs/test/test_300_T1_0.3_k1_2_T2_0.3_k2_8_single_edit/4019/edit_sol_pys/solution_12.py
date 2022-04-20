

def main():
    n, m, d = map(int, input().split())  # n:頂点数, m:辺の数, d:辺の最大長
    edges = [tuple(map(int, input().split())) for _ in range(m)]  # 辺のリスト

    if d == 0:  # 全ての頂点が1つの部分木に属する場合
        print('YES')
        for i in range(2, n+1):
            print(1, i)
    elif d == n-1:  # 全ての頂点が連結である場合
        print('YES')
        for i in range(2, n+1):
            print(i-1, i)
    else:  # それ以外の場合
        print('NO')

if __name__ == '__main__':
    main()
