

    """
    入力例
    3
    出力例
    4 2
    """
def main():
    K = int(input())
    N = 1
    while N <= K:
        N *= 2  # 1, 2, 4, 8, ...
    print(N, N // 2)

if __name__ == "__main__":
    main()
