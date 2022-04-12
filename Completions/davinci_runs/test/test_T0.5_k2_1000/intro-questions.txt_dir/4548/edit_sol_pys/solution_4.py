
def main():
    N, M, X = map(int, input().split())
    A = list(map(int, input().split()))
    if X == 0 or X == N:
        print(0)
        exit()

    # 左から、右に行くためのコスト
    left = 0
    # 右から、左に行くためのコスト
    right = 0
    # コストを計算する
    for i in range(X):
        if i in A:
            left += 1
    for i in range(X, N + 1):
        if i in A:
            right += 1
    print(min(left, right) + 1)


if __name__ == '__main__':
    main()
