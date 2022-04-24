

def main():
    N, M = map(int, input().split())  # N:人数 M:チーム数
    A = list(map(int, input().split()))
    total_votes = sum(A)
    if M == 1 and max(A) < total_votes / 4:
        print('No')
    elif max(A) < total_votes / (4 * M):
        print('No')
    else:
        print('Yes')


if __name__ == '__main__':
    main()
