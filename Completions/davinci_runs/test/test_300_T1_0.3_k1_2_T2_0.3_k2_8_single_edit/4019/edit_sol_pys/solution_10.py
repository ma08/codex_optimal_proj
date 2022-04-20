

def main():
    n, m, d = map(int, input().split())  # n: 頂点数, m: 辺の数, d: 各頂点からの最大距離
    edges = [tuple(map(int, input().split())) for _ in range(m)]  # 辺

    if d == 0:
        print('YES')  # 可能
        for i in range(2, n+1):  # 頂点1から各頂点への辺を追加
            print(1, i)  # 頂点1から頂点iへの辺を追加
    elif d == n-1:
        print('YES')  # 可能
        for i in range(2, n+1):  # 頂点1から各頂点への辺を追加
            print(i-1, i)  # 頂点i-1から頂点iへの辺を追加
    else:
        print('NO')  # 不可能

if __name__ == '__main__':
    main()
