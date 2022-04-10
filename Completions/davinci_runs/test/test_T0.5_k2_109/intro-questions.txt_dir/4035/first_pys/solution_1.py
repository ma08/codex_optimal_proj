

#-----main-----
a, b = map(int, input().split())

if a == b:
    # 消費税率が等しいとき、消費税が同じになるような最小の価格は、
    # 消費税を除いた価格が消費税率の分母で割り切れる整数となる
    price = a * 100 // 8
    if price * 8 == a * 100:
        print(price)
    else:
        print(-1)
else:
    # 消費税率が異なるとき、消費税が異なるような最小の価格は、
    # 消費税率が小さい方の消費税率の分母で割り切れる整数となる
    price = a * 100 // 8
    if price * 8 == a * 100:
        print(price)
    else:
        print(-1)