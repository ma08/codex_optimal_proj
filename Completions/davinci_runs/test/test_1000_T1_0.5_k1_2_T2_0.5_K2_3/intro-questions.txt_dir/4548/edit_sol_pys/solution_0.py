


def main():
    N, M, X = map(int, input().split())
    A = list(map(int, input().split()))

    # 左から、右に行くためのコストを計算
    left = 0
    # 右から、左に行くためのコストを計算
    right = 0
    # コストを計算する
    for i in range(X):
        if i+1 in A:
            left += 1
    for i in range(X, N):
        if i+1 in A:
            right += 1
    print(min(left, right))


if __name__ == '__main__':
    main()
