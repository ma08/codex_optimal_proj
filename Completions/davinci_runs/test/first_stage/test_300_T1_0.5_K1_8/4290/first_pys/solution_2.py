

def main():
    """
    全探索
    """
    N, M = map(int, input().split())
    # 奇数偶数で場合分け
    if (N + M) % 2 == 0:
        print((N + 1) * (M + 1) // 2)
    else:
        print(N * (M + 1) // 2 + M * (N + 1) // 2)

if __name__ == '__main__':
    main()