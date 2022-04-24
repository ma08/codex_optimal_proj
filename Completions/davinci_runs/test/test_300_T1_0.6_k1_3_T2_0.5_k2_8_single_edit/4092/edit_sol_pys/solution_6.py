

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0) # 0を先頭に挿入
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i + 1]
    d = {} # 各累積和をキーとする辞書
    ans = 0 # 答え
    for i in range(n):
        if s[i + 1] not in d: # s[i+1]がdにない場合
            d[s[i + 1]] = i + 1 # s[i+1]をキーとしてi+1を値とする
        else: # s[i+1]がdにある場合
            ans = max(ans, i + 1 - d[s[i + 1]]) # 答えを更新
    print(ans) # 答えを出力
    
if __name__ == "__main__":
    main()
