

def main():
    x = int(input()) # 入力
    if x >= 500: # 500円以上の場合
        coins = (x // 500) * 1000 + (x % 500) // 5 * 5 # 両替金額を計算
    else: # 500円未満の場合
        coins = x // 5 * 5 # 両替金額を計算
        
    print(coins) # 出力

if __name__ == '__main__':
    main()
