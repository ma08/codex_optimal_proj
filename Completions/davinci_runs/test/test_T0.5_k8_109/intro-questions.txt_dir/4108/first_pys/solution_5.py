


def main():
    S = input()
    T = input()
    # 単純に、文字列Sと文字列Tを比較する
    if S == T:
        print("Yes")
        return

    # 文字列Sに含まれる文字を、文字列Tに含まれる文字と比較する
    #   - 文字列Sに含まれる文字が文字列Tに含まれない場合、文字列Sと文字列Tは等しくない
    #   - 文字列Sに含まれる文字が文字列Tに含まれる場合、文字列Sと文字列Tは等しい
    for i in range(len(S)):
        if S[i] not in T:
            print("No")
            return
    print("Yes")


if __name__ == '__main__':
    main()