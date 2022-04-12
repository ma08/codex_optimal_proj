x = int(input().split()[0]) # x: 中央値
n = int(input().split()[0]) # n: 配列の長さ
p = [int(i) for i in input().split()] # p: 配列
p.sort() # 配列を昇順にソート

if x <= p[0]: # xが配列の最小値より小さい場合
    print(p[0]-x)
elif x >= p[-1]: # xが配列の最大値より大きい場合
    print(x-p[-1])
else: # xが配列の最小値と最大値の間の場合
    for i in range(1, n):
        if x <= p[i]: # xが配列のi番目の値より小さい場合
            print(min(x-p[i-1], p[i]-x))
            break
