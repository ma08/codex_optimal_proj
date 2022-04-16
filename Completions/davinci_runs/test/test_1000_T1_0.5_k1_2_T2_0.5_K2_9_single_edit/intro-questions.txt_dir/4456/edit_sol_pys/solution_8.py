

def main():
    n, k = map(int, input().split())   # 入力
    p = list(map(int, input().split()))    # 入力
    q = list(map(int, input().split()))    # 入力
    p = [i - 1 for i in p]   # 0始まりに変換
    q = [i - 1 for i in q]   # 0始まりに変換
    s = [None for i in range(n)]  # 文字列
    for i in range(k):    # 文字列を作る
        s[p[i]] = chr(ord("a") + i)    # 文字列を作る
        s[q[i]] = chr(ord("a") + i)    # 文字列を作る
    for i in range(k, n):     # 文字列を作る
        s[p[i]] = s[q[i]] = s[p[i - 1]]   # 文字列を作る
    print("YES")   # 出力
    print("".join(s))  # 出力

main()
