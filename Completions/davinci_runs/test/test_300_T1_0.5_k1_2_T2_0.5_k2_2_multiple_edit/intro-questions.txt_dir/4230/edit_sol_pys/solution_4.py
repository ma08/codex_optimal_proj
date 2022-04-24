x = int(input().split()[0]) # 主人公の位置
n = int(input().split()[0]) # ポケモンの数
p = [int(i) for i in input().split()] # ポケモンの位置
p.sort() # ポケモンの位置をソート

if x <= p[0]: # 主人公の位置が最初のポケモンより左
    print(p[0]-x) # 主人公の位置から最初のポケモンの位置を引く
elif x >= p[-1]: # 主人公の位置が最後のポケモンより右
    print(x-p[-1]) # 主人公の位置から最後のポケモンの位置を引く
else:
    for i in range(1, n):
        if x <= p[i]: # 主人公の位置がi番目のポケモンより左
            print(min(x-p[i-1], p[i]-x)) # 主人公の位置からi-1番目のポケモンの位置とi番目のポケモンの位置を引いたもののうち小さい方
            break
