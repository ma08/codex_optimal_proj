

x, y = map(int, input().split()) #x, yを文字列で受け取り、int型に変換してx, yに代入

if y % 2 == 0 and x * 2 <= y and y <= x * 4: #条件分岐
    print('Yes')
else:
    print('No')
