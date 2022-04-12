
import sys

def main():
    n, a, b = map(int, sys.stdin.readline().split()) # n, a, b を取得
    ans = 0

    for i in range(1, n+1): # 1からnまでループ
        s = str(i) # 数字を文字列に変換
        digit_sum = 0 # 各桁の和
        for c in s: # 文字列を1文字ずつ取り出す
            digit_sum += int(c) # 文字列を数字に変換して足していく

        if a <= digit_sum <= b: # 各桁の和がa以上b以下なら
            ans += i # 合計に足す

    print(ans)

if __name__ == "__main__":
    main()
