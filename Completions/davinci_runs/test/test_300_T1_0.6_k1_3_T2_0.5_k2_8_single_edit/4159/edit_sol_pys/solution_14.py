

a, b, k = map(int, input().split()) # a, b, k を入力

for i in range(k): # k回繰り返す
    if a > 0: # aが正の時
        a -= 1 # aを1減らす
    elif b > 0: # bが正の時
        b -= 1 # bを1減らす

print(a, b)
