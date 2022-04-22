

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    total_votes = sum(A)
    if max(A) < total_votes / (4 * M):  # 得票数が全員の得票数のM分の一以下の場合
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()
