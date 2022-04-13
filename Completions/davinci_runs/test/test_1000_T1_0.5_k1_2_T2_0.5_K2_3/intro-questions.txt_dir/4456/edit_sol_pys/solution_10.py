

def main():
    n, k = map(int, input().split())  # n: 問題数, k: 回答者1と回答者2が同じ問題数
    p = list(map(int, input().split()))  # p: 回答者1が正解した問題番号
    q = list(map(int, input().split()))  # q: 回答者2が正解した問題番号
    p = [i - 1 for i in p]  # 配列のインデックスを0からにする
    q = [i - 1 for i in q]  # 配列のインデックスを0からにする
    s = ["" for i in range(n)]  # 問題ごとに回答者が同じかどうかを表す文字列
    for i in range(k):  # 全ての問題に対して回答者が同じかどうかを判定
        s[p[i]] = chr(ord("a") + i)  # 回答者1が正解した問題番号の文字列をa, b, c,...に変換
        s[q[i]] = chr(ord("a") + i)  # 回答者2が正解した問題番号の文字列をa, b, c,...に変換
    for i in range(k, n):  # n - k個の問題を回答者が同じかどうかを判定
        s[p[i]] = s[q[i]] = s[p[i - 1]]  # 回答者1が正解した問題番号と回答者2が正解した問題番号の直前の問題番号の回答者が同じかどうかを判定
    print("YES")  # 回答者が同じかどうかを判定した文字列を出力
    print("".join(s))  # 回答者が同じかどうかを判定した文字列を出力

main()
