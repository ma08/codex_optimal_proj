

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))  # 各政党の投票数
    total_votes = sum(A)  # 合計投票数
    # 各政党の得票数の合計が総投票数の四分の一を超えているか
    if M == 1:
        if max(A) < total_votes / 4:
            print('No')
        else:
            print('Yes')
    else:
        if max(A) < total_votes / (4 * M):
            print('No')
        else:
            print('Yes')


if __name__ == '__main__':
    main()
