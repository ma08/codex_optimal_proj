

a, b, c = map(int, input().split())    # 入力を受け取る
order = input()                        # 入力を受け取る

if order == "ABC":                     # 順番がABCの場合は
    print(min(a, b, c), max(a, b, c) - min(a, b, c), max(a, b, c) - min(a, b, c))    # 出力する
elif order == "ACB":                   # 順番がACBの場合は
    print(min(a, b, c), max(a, b, c) - min(a, b, c), min(a, b, c))    # 出力する
elif order == "BAC":                   # 順番がBACの場合は
    print(max(a, b, c) - min(a, b, c), min(a, b, c), max(a, b, c) - min(a, b, c))    # 出力する
elif order == "BCA":                   # 順番がBCAの場合は
    print(max(a, b, c) - min(a, b, c), max(a, b, c) - min(a, b, c), min(a, b, c))    # 出力する
elif order == "CAB":                   # 順番がCABの場合は
    print(min(a, b, c), max(a, b, c) - min(a, b, c), min(a, b, c))    # 出力する
elif order == "CBA":                   # 順番がCBAの場合は
    print(max(a, b, c) - min(a, b, c), min(a, b, c), max(a, b, c) - min(a, b, c))    # 出力する
