def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))


    # 左から右に行くためのコストを計算
    left = sum([1 if i in A else 0 for i in range(N)])
    # 右から左に行くためのコストを計算
    right = sum([1 if i in A else 0 for i in range(N - 1, -1, -1)])
    print(min(left, right))


if __name__ == '__main__':
    main()
