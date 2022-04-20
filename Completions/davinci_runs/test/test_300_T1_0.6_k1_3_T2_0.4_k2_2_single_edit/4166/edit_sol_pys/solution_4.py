

def main():
    n, m = map(int, input().split()) # n:N,m:M
    a = [0] * n # a:配列
    for i in range(m): # m回繰り返す
        s, c = map(int, input().split()) # s:s番目,c:c
        a[s-1] = c # a[s-1]にcを代入
    for i in range(n): # n回繰り返す
        if i == 0 and a[i] == 0: # iが0かつa[i]が0のとき
            print(-1) # -1を出力
            return # 終了
        elif i == 0 and a[i] != 0: # iが0かつa[i]が0でないとき
            print(a[i], end="") # a[i]を出力
        else: # それ以外のとき
            print(a[i], end="") # a[i]を出力
    print("") # 改行

if __name__ == '__main__':
    main()
