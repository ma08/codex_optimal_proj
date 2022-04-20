

n, x, y = map(int, input().split()) # n: 桁数, x: 下からx桁目, y: 下からy桁目
num = input() # 入力される数字

if num[x] == '0':
    print(0)
else:
    print(1)
