

def main():
    n = int(input())  # 入力は1行のみ
    a = list(map(int, input().split()))  # map(int, input().split())で数値に変換してリスト化
    mx = max(a)  # max関数で最大値
    mn = min(a)  # min関数で最小値
    if mx == mn:  # 最大値と最小値が一緒ならば
        print('YES')  # YES
        return  # returnで終了
    if mx - mn > 1:  # 最大値と最小値の差が1より大きいならば
        print('NO')  # NO
        return  # returnで終了
    if a.count(mx) > 1 and a.count(mn) > 1:  # 最大値と最小値の出現回数が1より大きいならば
        print('NO')  # NO
        return  # returnで終了
    print('YES')  # それ以外ならばYES


if __name__ == "__main__":
    main()
