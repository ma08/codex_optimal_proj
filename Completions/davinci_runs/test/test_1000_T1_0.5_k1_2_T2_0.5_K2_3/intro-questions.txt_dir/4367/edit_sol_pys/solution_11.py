
n, r = map(int, input().split())  # 2つの数字をスペース区切りで入力し、nとrに代入

if n >= 10:  # nが10以上ならば
    print(r)
else:
    print(r + 100 * (10 - n))
