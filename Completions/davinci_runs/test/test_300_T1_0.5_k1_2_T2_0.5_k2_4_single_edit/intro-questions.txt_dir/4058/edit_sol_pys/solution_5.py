

def get_input():
    n, r = [int(x) for x in input().split()] # n: 数列の長さ, r: 半径
    a = [int(x) for x in input().split()] # a: 数列
    return n, r, a # 数列の長さ, 半径, 数列

def solve(n, r, a):
    ans = 0 # アンテナの数
    i = 1 # 先頭のインデックス
    while i <= n:
        if a[i-1] == 0: # 数列のi番目が0なら
            j = i # jをiとする
            while j <= n and a[j-1] == 0: # jがn以内かつj番目が0なら
                j += 1
            if j - i + 1 > 2*r: # iからjまでの距離が2rを超えるなら
                return -1
            if j <= n: # jがn以下なら
                a[j-1] = 1 # j番目を1にする
                ans += 1 # アンテナを1個増やす
            else:
                return -1
            i = j # iをjとする
        else: # 数列のi番目が0でないなら
            i += 1
    return ans # アンテナの数

def main():
    n, r, a = get_input()
    ans = solve(n, r, a)
    print(ans)

if __name__ == '__main__':
    main()
