

#-----main-----
a, b = map(int, input().split())

if a == b:
    # 税率が等しいとき、税が同じになるような最小の価格は、
    # 税を除いた価格が税率の分母で割り切れる整数となる
    price = a * 100 // 8
    if price * 8 == a * 100:
        print(price)
    else:
        print(-1)
else:
    # 税率が異なるとき、税が異なるような最小の価格は、
    # 税率が小さい方の税率の分母で割り切れる整数となる
    price = b * 100 // 10
    if price * 10 == b * 100:
        print(price)
    else:
        print(-1)
