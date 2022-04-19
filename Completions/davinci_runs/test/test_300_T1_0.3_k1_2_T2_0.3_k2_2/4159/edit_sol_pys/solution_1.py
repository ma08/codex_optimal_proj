

a, b, k = map(int, input().split())  # a, b, kを受け取る

while k > 0:  # kが0より大きい間
    if a > 0:  # aが0より大きい間
        a -= 1  # aを1引く
    elif b > 0:  # bが0より大きい間
        b -= 1  # bを1引く
    k -= 1  # kを1引く

print(a, b)
