

def main():
    """
    N, K = map(int, input().split())
    L = list(map(int, input().split()))

    L.sort(reverse=True)
    print(sum(L[:K]))
    """
    N, K = map(int, input().split())  # 標準入力を二つの数値として取得
    L = sorted(map(int, input().split()), reverse=True)  # 標準入力を数値のリストとして取得して降順にソート
    print(sum(L[:K]))

if __name__ == '__main__':
    main()
