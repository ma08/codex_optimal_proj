
a, b, k = map(int, input().split())

if k <= a:  # kがaより小さい時
    a -= k  # aからkを引く
else:  # kがaより大きい時
    k -= a  # kからaを引く
    a = 0  # aを0にする
    if k <= b:  # kがbより小さい時
        b -= k  # bからkを引く
    else:
        b = 0

print(a,b)
