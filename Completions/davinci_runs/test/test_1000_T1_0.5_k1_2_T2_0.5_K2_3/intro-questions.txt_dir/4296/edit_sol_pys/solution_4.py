

a1,a2,a3 = map(int, input().split()) # 入力を受け取り、スペースで区切って整数型に変換する

if a1 + a2 + a3 >= 22: 
    print('bust') # 合計が22以上であればbustを出力
else:
    print('win')
