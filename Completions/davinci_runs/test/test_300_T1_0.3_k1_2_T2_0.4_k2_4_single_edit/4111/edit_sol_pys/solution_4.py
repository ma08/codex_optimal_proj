

def main():
    n = int(input()) # 数列の長さ
    a = list(map(int, input().split())) # 数列
    odd = 0 # 奇数番目の合計
    even = 0 # 偶数番目の合計
    count = 0 # 差が0になる回数
    for i in range(n): # 奇数番目の合計と偶数番目の合計を算出
        if i % 2 == 0: # 偶数番目
            even += a[i] # 偶数番目の合計に加算
        else: # 奇数番目
            odd += a[i] # 奇数番目の合計に加算
    for i in range(n): # 差が0になる回数を算出
        if i % 2 == 0: # 偶数番目
            even -= a[i] # 偶数番目の合計から除算
        else: # 奇数番目
            odd -= a[i] # 奇数番目の合計から除算
        if even == odd: # 差が0のとき
            count += 1 # 差が0になる回数を1加算
        if i % 2 == 0: # 偶数番目
            even += a[i] # 偶数番目の合計に加算
        else: # 奇数番目
            odd += a[i] # 奇数番目の合計に加算
    print(count) # 差が0になる回数を出力

if __name__ == "__main__":
    main()
