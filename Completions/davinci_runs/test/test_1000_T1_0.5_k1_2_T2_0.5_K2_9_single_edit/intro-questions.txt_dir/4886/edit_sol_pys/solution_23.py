
def main():
    N, K = map(int, input().split())  # N:人数、K:言いたいこと
    if K >= N:  # KがN以上だったら
        print('Your wish is granted!')  # あなたの願いは叶う
    else:  # KがN未満だったら
        print('You will become a flying monkey!')  # あなたは空を飛ぶサルになる

if __name__ == '__main__':
    main()
