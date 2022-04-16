

A, B = map(int, input().split())  # スペース区切りの整数の入力

if A <= 5:
    print(0)
elif A <= 12:
    print(B // 2)  # 小数点以下切り捨て
else:
    print(0)
