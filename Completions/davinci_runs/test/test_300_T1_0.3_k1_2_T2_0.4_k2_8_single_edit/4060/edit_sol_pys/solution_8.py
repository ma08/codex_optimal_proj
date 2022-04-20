
n = int(input())  # 文字列の長さ
s = input()  # 文字列
if n % 2 == 1:  # 文字列の長さが奇数なら
    print(0)  # 0を出力
else:  # 偶数なら
    cnt = 0  # cntを0で初期化
    for i in range(n):  # 文字列の長さ分ループ
        if s[i] == '(':  # 文字列のi番目が'('なら
            cnt += 1  # cntをインクリメント
        else:  # ')'なら
            cnt -= 1  # cntをデクリメント
        if cnt < 0:  # cntが負なら
            print(0)  # 0を出力
            break  # ループを抜ける
    else:  # ループが終了したら
        print(cnt // 2)  # cntを2で割った商を出力
