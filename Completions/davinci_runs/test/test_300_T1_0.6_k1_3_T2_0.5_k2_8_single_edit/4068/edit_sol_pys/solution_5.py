
# coding: utf-8

    # N 段の階段を上るとき、1 段につき 1 歩か 2 歩かで上ることができる。
    # このとき、何通りの選び方があるか求めよ。
    # ただし、階段の上り方は、階段の途中でも段を戻ってはならない。
    # また、階段を上るときには、どの段を使うかが決まっているものとする。
    # つまり、1 歩で 2 段目に上るときは、1 段目を使うものとする。
def main():
    N, M = [int(i) for i in input().split()]
    dp = [0] * (N + 2)

    # 階段の途中でも段を戻ってはならないので、「戻れない段」を設定する
    a = set()
    for i in range(M):
        ai = int(input())  # 戻れない段
        a.add(ai)  # 集合に追加

    # 初期化
    dp[0] = 1  # 0 段目は 1 通り
    if 1 not in a:
        dp[1] = 1

    # dp[i] → dp[i + 1] の更新
    for i in range(N):
        if i + 1 not in a:
            dp[i + 1] = (dp[i + 1] + dp[i]) % (10 ** 9 + 7)
        if i + 2 not in a:
            dp[i + 2] = (dp[i + 2] + dp[i]) % (10 ** 9 + 7)

    print(dp[N])


if __name__ == '__main__':
    main()
