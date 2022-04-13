
a, b, c, d = map(int, input().split()) # 入力
if d >= abs(a - c): # dがaとcの差以上の場合
    print('Yes') # Yesを出力
elif d >= abs(a - b) and d >= abs(b - c): # dがaとbの差とbとcの差のどちらか以上の場合
    print('Yes') # Yesを出力
else:
    print('No')
