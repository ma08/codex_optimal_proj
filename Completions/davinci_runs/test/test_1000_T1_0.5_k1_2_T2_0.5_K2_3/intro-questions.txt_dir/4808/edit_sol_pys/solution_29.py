

def main():
    n, d = map(int, input().split()) #入力を受け取る
    ds = list(map(int, input().split())) #入力を受け取る
    ds.append(d) #dsにdを追加
    count = 0 #countを0に初期化
    for i in range(len(ds)): #dsの要素数分繰り返す
        if ds[i] > ds[-1]: #ds[i]がds[-1]より大きい場合
            count += 1 #countに1を足す
        else: #そうでない場合
            break #ループを抜ける
    if count == 0: #countが0の場合
        print("It had never snowed this early in {} years!".format(count)) #countの値を出力
    else: #そうでない場合
        print("It hadn't snowed this early in {} years!".format(count)) #countの値を出力

if __name__ == "__main__":
    main()
