


def main():
    n, k = map(int, input().split())  # n:問題数,k:時間
    problems = list(map(int, input().split()))
    ans = 0
    while len(problems) > 0:  # 問題がある限り繰り返す
        if problems[0] <= k:  # 問題が解ける場合
            ans += 1  # 解いた問題数を1問増やす
            problems.pop(0)  # 問題を取り除く
        elif problems[-1] <= k:  # 問題が解ける場合
            ans += 1  # 解いた問題数を1問増やす
            problems.pop()  # 問題を取り除く
        else:  # 問題が解けない場合
            break  # 繰り返しをやめる
    print(ans)


if __name__ == '__main__':
    main()
