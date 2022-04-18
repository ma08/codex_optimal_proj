

a, b, c = map(int, input().split())    # 入力
order = input()                        # 入力

if order == "ABC":                     # 順番がABCの場合
    print(min(a, b, c), max(a, b, c) - min(a, b, c), max(a, b, c) - min(a, b, c))
elif order == "ACB":                   # 順番がACBの場合
    print(min(a, b, c), max(a, b, c) - min(a, b, c), min(a, b, c))
elif order == "BAC":                   # 順番がBACの場合
    print(max(a, b, c) - min(a, b, c), min(a, b, c), max(a, b, c) - min(a, b, c))
elif order == "BCA":                   # 順番がBCAの場合
    print(max(a, b, c) - min(a, b, c), max(a, b, c) - min(a, b, c), min(a, b, c))    # 出力
elif order == "CAB":                   # 順番がCABの場合
    print(min(a, b, c), max(a, b, c) - min(a, b, c), min(a, b, c))    # 出力
elif order == "CBA":                   # 順番がCBAの場合
    print(max(a, b, c) - min(a, b, c), min(a, b, c), max(a, b, c) - min(a, b, c))    # 出力
