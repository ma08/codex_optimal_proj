

def main():
    n, a = map(int, input().split()) #n,aを受け取る
    w = list(map(int, input().split())) #wを受け取る
    w.sort() #wをソート
    i = 0
    while a > 0 and i < n: #aが0より大きく、iがnより小さい間
        if a >= w[i]: #aがw[i]以上なら
            a -= w[i] #aからw[i]を引く
            i += 1 #iをインクリメント
        else:
            break #それ以外ならbreak
    print(i) #iを出力

if __name__ == "__main__":
    main()
