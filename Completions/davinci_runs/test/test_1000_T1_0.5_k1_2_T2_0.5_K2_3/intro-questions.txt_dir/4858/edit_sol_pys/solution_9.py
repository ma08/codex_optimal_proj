

def main():
    M, N, C = input().split()   # M=行数 N=列数 C=文字
    M = int(M)                  # Mをint型に変換
    N = int(N)                  # Nをint型に変換
    first = []                  # 1つ目の文字列を格納するリスト
    second = []                 # 2つ目の文字列を格納するリスト
    for i in range(M):          # 1つ目の文字列を入力する
        first.append(list(input()))  # 1つ目の文字列をリストに格納
    for i in range(M):          # 2つ目の文字列を入力する
        second.append(list(input()))  # 2つ目の文字列をリストに格納
    for i in range(M):          # 1つ目の文字列を処理する
        for j in range(N):      # 列数分繰り返す
            if first[i][j] != C:  # 1つ目の文字列がCでなければ
                first[i][j] = '.'  # firstのi行j列目を'.'に変換
            else:                  # 1つ目の文字列がCであれば
                first[i][j] = 'x'  # firstのi行j列目を'x'に変換
            if second[i][j] != C:  # 2つ目の文字列がCでなければ
                second[i][j] = '.'  # secondのi行j列目を'.'に変換
            else:                  # 2つ目の文字列がCであれば
                second[i][j] = 'x'  # secondのi行j列目を'x'に変換
    for i in range(M):          # 2つ目の文字列を処理する
        for j in range(N):      # 列数分繰り返す
            if second[i][j] == 'x' and first[i][j] != 'x':  # 2つ目の文字列がCで1つ目の文字列がCでないなら
                second[i][j] = '^'  # secondのi行j列目を'^'に変換
    for i in range(M):          # 2つ目の文字列を処理する
        for j in range(N):      # 列数分繰り返す
            if second[i][j] == '^':  # 2つ目の文字列が'^'なら
                second[i][j] = '.'  # secondのi行j列目を'.'に変換
            if second[i][j] == 'x':  # 2つ目の文字列が'x'なら
                second[i][j] = C    # secondのi行j列目をCに変換
    for i in range(M):          # 2つ目の文字列を出力する
        print(''.join(second[i]))  # 2つ目の文字列を出力
    print()  # 改行

if __name__ == '__main__':
    main()
