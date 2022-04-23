
a, b, c, k = map(int, input().split()) # 入力

if k <= a:
    print(k) # kがa以下の時
elif k <= a + b:
    print(a) # kがa以上b以下の時
else:
    print(a - (k - (a + b)))
