
import sys
import math

def main():
    n = int(input())  # 入力
    s = input()  # 入力
    l = len(s)  # 文字列の長さ
    dp = [[0] * (n + 1) for i in range(l + 1)]  # DPテーブル
    ans = 0  # 答え
    for i in range(l):  # 最初の文字が(ならば
        if s[i] == '(':  # 左端が(ならば
            dp[i][0] = 1  # それは有効
    for i in range(l):  # 文字列を順に見ていく
        for j in range(n):  # 左端からj個の(を取っている状態
            if dp[i][j] == 0:  # 0ならば有効ではないのでスキップ
                continue  # スキップ
            if s[i] == '(':  # (ならば
                dp[i + 1][j] += dp[i][j]  # 次の文字列でj個の(を取る
                dp[i + 1][j + 1] += dp[i][j]  # 次の文字列でj+1個の(を取る
            else:  # )ならば
                if j > 0:  # jが0でないならば
                    dp[i + 1][j - 1] += dp[i][j]  # 次の文字列でj-1個の(を取る
    for i in range(n + 1):  # 全ての文字列で
        ans += dp[l][i]  # 左端がi個の(を取るパターンを足す
    print(ans)  # 表示

if __name__ == "__main__":
    main()
